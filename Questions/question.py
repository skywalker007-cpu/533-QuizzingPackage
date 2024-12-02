from collections import UserDict


class Question(UserDict):
    """
    Question class to store question data within a dictionary format. We extend the UserDict class to
    allow us to use the data attribute to access the nested dictionary.
    """

    def __init__(self, question_id, question_text, correct_answer, score=1):
        super().__init__()
        self.data["Q_id"] = question_id
        self.data["question"] = question_text
        self.data["answer"] = correct_answer
        self.data["score"] = score

    def __str__(self):
        return f"ID: {self.data['Q_id']}, Question: {self.data['question']}, Score: {self.data['score']}"

    def __eq__(self, other):
        return self.data["Q_id"] == other.data["Q_id"] and self.data["question"] == other.data["question"] and \
               self.data["answer"] == other.data["answer"] and self.data["score"] == other.data["score"]

class MultipleChoice(Question):
    """
    Multiple choice class to store multiple choice question data.
    """

    def __init__(self, question_id, question_text, correct_answer, score=1, options=None):
        super().__init__(question_id, question_text, correct_answer, score)
        if options is None:
            options = []
        self.data["options"] = options

    def __str__(self):
        for option in self.data["options"]:
            return f"{super().__str__()}\nOptions:\n{option}"


class ShortAnswerQuestion(Question):
    """
    Short answer question class to store short answer question data.
    """

    def __init__(self, question_id, question_text, correct_answer, score=1, notice=None):
        super().__init__(question_id, question_text, correct_answer, score)
        # notice attribute can be something like "please answer in one sentence"
        if notice is None:
            notice = ""
        self.data["notice"] = notice

    def __str__(self):
        notification = self.data["notice"]
        return f"{super().__str__()}\nNote:\n{notification}"


class TrueFalseQuestion(Question):
    """
    True false question class to store true false question data.
    """

    def __init__(self, question_id, question_text, correct_answer, score=1, options=None):
        super().__init__(question_id, question_text, correct_answer, score)
        if options is None:
            options = ["True", "False"]
        self.data["options"] = options

    def __str__(self):
        return f"{super().__str__()}\nOptions:\nTrue\nFalse"
