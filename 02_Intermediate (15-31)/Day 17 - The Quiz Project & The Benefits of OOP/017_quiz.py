from question_model import Question
from quiz_brain import Quizbrain
import data

question_bank = []

for question in data.new_question_data:
    new_question = Question(question['text'], question['answer'])
    question_bank.append(new_question)

quiz = Quizbrain(question_bank)
while quiz.still_has_questions():
    answer = quiz.next_question()

print("="*25)
print("End of the Quiz")
print(f"Final Score: {quiz.score}/{quiz.question_number}")
print("="*25)



