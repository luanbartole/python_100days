from tkinter import *

FONT = ("Arial", 12)

window = Tk()
window.title("Kg to Lb")
window.minsize(width=220, height=100)

entry = Entry(width=10)
entry.insert(END, string="0")
entry.grid(column=1, row=0)

label0 = Label(text="Kg", font=FONT)
label0.grid(column=2, row=0)

label1 = Label(text="Is equal to", font=FONT)
label1.grid(column=0, row=1)

label2 = Label(text="0", font=FONT)
label2.grid(column=1, row=1)

label3 = Label(text="lb", font=FONT)
label3.grid(column=2, row=1)

def action():
    lb_number = int(entry.get()) * 2.20462
    label2["text"] = f"{lb_number:.2f}"

button = Button(text="Convert", command=action)
button.grid(column=1, row=2)

window.mainloop()
