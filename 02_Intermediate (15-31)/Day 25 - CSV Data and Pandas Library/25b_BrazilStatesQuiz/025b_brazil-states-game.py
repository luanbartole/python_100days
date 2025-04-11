import turtle, pandas
from guess import Guess

screen = turtle.Screen()
screen.setup(width=1000, height=1000)
screen.title("Brazil States Game by Luan Bartole")
image = "brazil_map.gif"
screen.addshape(image)
turtle.shape(image)

df = pandas.read_csv("brazil_states.csv")
guess = Guess(screen)

guess.quiz_the_user()
turtle.mainloop()