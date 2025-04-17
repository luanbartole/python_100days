from question_model import Question
from quiz_brain import Quizbrain
import data
from ui import QuizInterface

# Build the list of Question objects from raw API data
question_bank = []
for question in data.new_question_data:
    new_question = Question(question['question'], question['correct_answer'])
    question_bank.append(new_question)

# Initialize quiz logic and user interface
quiz = Quizbrain(question_bank)
quiz_ui = QuizInterface(quiz)

# Print final result in the console after GUI closes
print("=" * 25)
print("End of the Quiz")
print(f"Final Score: {quiz.score}/{quiz.question_number}")
print("=" * 25)
