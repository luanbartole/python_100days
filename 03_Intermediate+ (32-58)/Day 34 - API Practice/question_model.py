class Question:
    """
    Represents a single quiz question with its text and correct answer.
    """

    def __init__(self, text, answer):
        """
        Initialize a question with the given text and answer.

        :param text: The question text (str)
        :param answer: The correct answer (str), usually "True" or "False"
        """
        self.text = text
        self.answer = answer
