from turtle import Turtle
import pandas
from PIL.ImageChops import screen

# Maximum number of guesses allowed
TRIES = 27

# Load data from CSV file
BRAZIL_STATES = pandas.read_csv("brazil_states.csv")
STATES_LIST = BRAZIL_STATES.state.tolist()     # List of state names
STATES_ACR = BRAZIL_STATES.acronym              # List of state acronyms
X_LIST = BRAZIL_STATES.x                        # List of X coordinates for map placement
Y_LIST = BRAZIL_STATES.y                        # List of Y coordinates for map placement
FONT = ("Arial", 40, "bold")

class Guess(Turtle):
    """
    A class that handles the logic of the Brazil States guessing game.
    Inherits from Turtle to allow writing directly on the map.
    """

    def __init__(self, window):
        """
        Initialize the Guess object.

        Args:
            window: The turtle screen where the game is displayed.
        """
        super().__init__()
        self.hideturtle()
        self.penup()
        self.correct_tries = 0                  # Number of correct guesses
        self.screen = window                    # Reference to the main turtle screen
        self.correct_states_list = []           # List of correctly guessed states

    def quiz_the_user(self):
        """
        Run the main guessing loop. Prompts the user up to TRIES times
        to guess Brazilian states and displays the correct ones on the map.
        """
        for _ in range(TRIES):

            answer_state = self.screen.textinput(
                title=f"{self.correct_tries}/27 Correct tries",
                prompt="State Name:"
            )

            if not answer_state:
                break  # Skip if user presses cancel or gives empty input

            answer_state = answer_state.title()  # Normalize capitalization
            correct_state = self.check_state(answer_state)

            if correct_state is not None:
                self.correct_tries += 1
                self.correct_states_list.append(correct_state)
                self.write_state(STATES_LIST.index(correct_state))

        self.game_over()

    def check_state(self, answer):
        """
        Check if the user's answer is a valid and not-yet-guessed state.

        Args:
            answer (str): The name of the guessed state.

        Returns:
            str or None: The correct state name if valid, otherwise None.
        """
        if answer in STATES_LIST and answer not in self.correct_states_list:
            return answer

    def write_state(self, state_id):
        """
        Write the acronym of the state on the map at the correct position.

        Args:
            state_id (int): The index of the state in the CSV/state list.
        """
        self.goto(X_LIST[state_id], Y_LIST[state_id])
        self.write(STATES_ACR[state_id], align="center", font=("Courier", 10, "bold"))

    def game_over(self):
        """
        Display 'GAME OVER' and the number of correct guesses on the screen.

        This method writes the final result in the bottom-left corner of the map.
        """
        self.screen.tracer(0)
        self.goto(-450, -300)
        self.write("GAME OVER", font=FONT)
        self.goto(-350,-350)
        self.write(f"{self.correct_tries}/27", font=FONT)
        self.screen.update()
