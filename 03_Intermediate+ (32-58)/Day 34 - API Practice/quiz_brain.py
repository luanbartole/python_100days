import html

class Quizbrain:
    """
    Handles the quiz logic: fetching questions, checking answers,
    and tracking the score and progress.
    """

    def __init__(self, q_list):
        """
        Initialize the quiz with a list of questions.

        :param q_list: List of Question objects
        """
        self.question_number = 0
        self.question_list = q_list
        self.score = 0
        self.current_question = ""

    def next_question(self):
        """
        Retrieve the next question, update the current question,
        and return the formatted question string.

        :return: Formatted question string (str)
        """
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {q_text}"

    def still_has_questions(self):
        """
        Check if there are more questions left.

        :return: True if more questions are available, else False
        """
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        """
        Compare user answer with the correct answer, update score if correct.

        :param user_answer: User's answer (str)
        :param correct_answer: Actual correct answer (str)
        :return: True if correct, else False
        """
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False
