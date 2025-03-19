class Question:
    """
    Represents a quiz question with its corresponding answer.

    Attributes:
        text (str): The text of the question.
        answer (bool): The correct answer to the question (True or False).

    Methods:
        __init__(self, text, answer): Initializes a Question object with the question's text and the correct answer.
        __str__(self): Returns a string representation of the Question object, showing the question and its answer.
        check_answer(self, user_input): Compares the user's input with the correct answer and returns True if they match, otherwise False.
    """

    def __init__(self, text, answer):
        """
        Initializes a new Question object with the given question text and answer.

        Args:
            text (str): The question text.
            answer (bool): The correct answer (True or False).
        """
        self.text = text  # Store the question text
        self.answer = answer  # Store the correct answer (True/False)

    def __str__(self):
        """
        Returns a string representation of the Question object, useful for debugging and displaying the question.

        Returns:
            str: A string that describes the Question object, showing the question and its correct answer.
        """
        return f"Question: {self.text}, Answer: {self.answer}"

    def check_answer(self, user_input):
        """
        Compares the user's input with the correct answer and returns a boolean value.

        Args:
            user_input (bool): The user's answer (True or False).

        Returns:
            bool: True if the user's answer matches the correct answer, False otherwise.
        """
        return self.answer == user_input  # Return True if the answer is correct, else False
