from tkinter import *
from quiz_brain import Quizbrain

THEME_COLOR = "#375362"

class QuizInterface:
    """
    UI class for the quiz app using tkinter.
    It interfaces with the Quizbrain logic to display questions and handle user input.
    """

    def __init__(self, quiz_brain: Quizbrain):
        """
        Initialize the GUI, set up layout and display the first question.
        """
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler by Luan Bartole")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Score display label
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        # Canvas for question text
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150, 125,
            width=250,
            text="Some Question Text",
            font=("Arial", 16, "italic"),
            fill=THEME_COLOR
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # True button
        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)

        # False button
        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        """
        Fetch and display the next question.
        Ends the quiz if no questions remain.
        """
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}/{self.quiz.question_number}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        """
        Handler for the True button.
        Checks answer and gives feedback.
        """
        is_right = self.quiz.check_answer("true", self.quiz.current_question.answer)
        self.give_feedback(is_right)

    def false_pressed(self):
        """
        Handler for the False button.
        Checks answer and gives feedback.
        """
        is_right = self.quiz.check_answer("false", self.quiz.current_question.answer)
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        """
        Changes canvas color based on whether answer was correct,
        then moves to the next question after a short delay.
        """
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
