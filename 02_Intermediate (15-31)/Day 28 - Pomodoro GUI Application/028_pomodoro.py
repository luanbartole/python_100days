from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
# Color themes for different session types
FOCUS_COLOR = "#BA4949"
SHORT_BREAK_COLOR = "#38858A"
LONG_BREAK_COLOR = "#397097"
TEXT_COLOR = "#FFFFFF"

# Font used across the app
FONT_NAME = "Arial Rounded MT Bold"

# Durations for work and breaks (in minutes)
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# Timer speed (for testing: 1 means it counts down in real time)
SET_TIMER = 1000  # Set to 1000 for actual seconds in production

# Tracking repetitions and the timer
reps = 0
timer = None
is_paused = False



# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    """
    Resets the timer to initial state:
    - Stops the current countdown
    - Resets session count
    - Resets timer text and checkmarks
    - Updates UI to default focus session
    """
    global reps, is_paused, timer
    if timer:
        window.after_cancel(timer)
        timer = None
    reps = 0
    is_paused = False
    update_ui("Focus Time", FOCUS_COLOR, "25:00", 0)


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    """
    Starts the timer based on the Pomodoro cycle:
    - Work sessions on odd reps
    - Short breaks on even reps
    - Long break every 8th rep
    Updates the UI accordingly before starting countdown
    """
    global reps, is_paused
    if timer:
        window.after_cancel(timer)

    if is_paused:
        # Resume the timer
        is_paused = False
        current_time = canvas.itemcget(timer_text, "text")
        minutes, seconds = map(int, current_time.split(":"))
        count = minutes * 60 + seconds
        count_down(count)
        return

    reps += 1

    # Convert minutes to seconds
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # Choose session type based on reps and start countdown
    if reps % 8 == 0:
        update_ui("Long Break", LONG_BREAK_COLOR, LONG_BREAK_MIN, reps)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        update_ui("Short Break", SHORT_BREAK_COLOR, SHORT_BREAK_MIN, reps)
        count_down(short_break_sec)
    else:
        update_ui("Focus Time", FOCUS_COLOR, WORK_MIN, reps)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    """
    Recursive countdown function that:
    - Updates the timer every second
    - Displays MM:SS format
    - Calls start_timer() again when countdown reaches zero
    """
    global timer
    if is_paused:
        return  # Stop countdown if paused

    minutes = math.floor(count / 60)
    seconds = count % 60
    canvas.itemconfig(timer_text, text=f"{minutes:02d}:{seconds:02d}")

    if count > 0:
        timer = window.after(SET_TIMER, count_down, count - 1)
    else:
        start_timer()

# ---------------------------- PAUSE TIMER ------------------------------- #
def pause_timer():
    """
    Pauses the timer by setting the is_paused flag and cancelling the scheduled countdown.
    """
    global is_paused
    is_paused = True
    window.after_cancel(timer)



# ---------------------------- UI UPDATE ------------------------------- #
def update_ui(title, color, time_display, progress):
    """
    Updates the appearance of the app based on session type:
    - Changes colors (background and buttons)
    - Updates the session title and timer
    - Shows check dots for completed work sessions
    """
    # Change overall background colors
    elements_to_color = [
        window, card_frame, canvas, button_frame,
        start_btn, pause_btn, reset_btn, title_label
    ]
    for element in elements_to_color:
        element.config(bg=color)

        # Update title text
        title_label.config(text=title)

    # Format the time (int to MM:00 or use string directly)
    time_str = f"{time_display:02d}:00" if isinstance(time_display, int) else time_display
    canvas.itemconfig(timer_text, text=time_str)

    # Show one ● per completed work session (every 2 reps)
    check_dots.config(text="● " * (progress // 2), fg=TEXT_COLOR, bg=color)


# ---------------------------- UI SETUP ------------------------------- #
# Initialize main window
window = Tk()
window.title("Pomodoro by Luan Bartole")
window.config(padx=40, pady=40, bg=FOCUS_COLOR)

# Card Frame: holds all core content
card_frame = Frame(window, bg=FOCUS_COLOR, bd=0, relief=FLAT)
card_frame.grid(column=1, row=0)

# Title Label: shows "Focus Time", "Short Break", etc.
title_label = Label(card_frame, text="Focus Time", font=(FONT_NAME, 20), fg=TEXT_COLOR, bg=FOCUS_COLOR)
title_label.grid(column=0, row=0, pady=(0, 20))

# Timer Canvas: circular countdown timer
canvas = Canvas(card_frame, width=200, height=200, bg=FOCUS_COLOR, highlightthickness=0)
circle = canvas.create_oval(10, 10, 190, 190, outline=TEXT_COLOR, width=2)
timer_text = canvas.create_text(100, 100, text="25:00", fill=TEXT_COLOR, font=(FONT_NAME, 28, "bold"))
canvas.grid(column=0, row=1)

# Buttons Frame: holds Start and Reset buttons
button_frame = Frame(card_frame, bg=FOCUS_COLOR)
button_frame.grid(column=0, row=3, pady=20)

# ▶ Start button
start_btn = Button(button_frame, text="▶", font=(FONT_NAME, 14), command=start_timer, bg=FOCUS_COLOR, fg=TEXT_COLOR, bd=0)
start_btn.grid(column=0, row=0, padx=10)

# ⏸ Pause button
pause_btn = Button(button_frame, text="⏸", font=(FONT_NAME, 14), command=pause_timer, bg=FOCUS_COLOR, fg=TEXT_COLOR, bd=0)
pause_btn.grid(column=1, row=0, padx=10)

# ⏭ Reset button
reset_btn = Button(button_frame, text="⏭", font=(FONT_NAME, 14), command=reset_timer, bg=FOCUS_COLOR, fg=TEXT_COLOR, bd=0)
reset_btn.grid(column=2, row=0, padx=10)

# Progress Dots: displayed just below the canvas
check_dots = Label(card_frame, text="", font=(FONT_NAME, 14), fg=TEXT_COLOR, bg=FOCUS_COLOR)
check_dots.grid(column=0, row=4)

# Start the app loop
window.mainloop()
