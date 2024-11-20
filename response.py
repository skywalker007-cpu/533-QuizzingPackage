class Response:
    """
    Response class: each student with unique id and their corresponding answers for the quiz.
    """
    def __init__(self, student_id, response):
        self.student_id = student_id
        self.response = response

    def __str__(self):
        return f"Student ID: {self.student_id}, Responses to the quiz: {self.response}"
