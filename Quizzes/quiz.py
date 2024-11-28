from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import Questions.question as question
from Responses.response import Response


class Quiz:
    def __init__(self, title = "untitled_quiz", questions = None):
        self.title = title
        self.total_score = 0

        self.questions = {}
        self.responses = {}
        self.marks = {}
        if questions is not None:
            self.add_questions(questions)

    def __str__(self):
        return f"\n\nQuiz_Title: {self.title} \n\nTotal_Score: {self.total_score} \n\nQuestions: {self.questions} \n\nResponses: {self.responses}"

    def __eq__(self, other):
        def compare_questions(q1, q2):
            if len(q1) != len(q2):
                return False
            for key, value in q1.items():
                if key not in q2 or value != q2[key]:
                    return False
            return True
        return self.title == other.title and self.total_score == other.total_score and compare_questions(self.questions, other.questions)
    
    def clone(self):
        """
        Clone the quiz object.
        :return: Quiz object
        """
        return Quiz(self.title, self.questions.copy())

    def add_questions(self, questions=None):
        """
        Add a question or a list of questions to the quiz.
        :param questions: Question or list of questions to be added to the quiz.
        :raises Exception: If the question is not a valid question type.
        :raises Exception: If the question ID already exists in the quiz.
        :return: None
        """        
        try:
            if self.responses:
                raise Exception("Responses Error: Cannot add questions to a quiz with responses")
            if isinstance(questions, list):
                for q in questions:
                    if isinstance(q, question.Question):
                        if q.data["Q_id"] in self.questions:
                            raise Exception(
                                "Duplicate ID Error: Question ID " + str(q.data["Q_id"]) + " already exists")
                        self.questions[q.data["Q_id"]] = q
                        self.total_score += q.data["score"]
                    else:
                        raise Exception("Invalid Type Error:" + str(type(q)) + " is not a valid question type")
            elif isinstance(questions, dict):
                for key, value in questions.items():
                    if isinstance(value, question.Question):
                        if value.data["Q_id"] in self.questions:
                            raise Exception(
                                "Duplicate ID Error: Question ID " + str(value.data["Q_id"]) + " already exists")
                        if value.data["Q_id"] != key:
                            raise Exception("ID Mismatch Error: Question ID " + str(
                                value.data["Q_id"]) + " does not match the key " + str(key))
                        self.questions[value.data["Q_id"]] = value
                        self.total_score += value.data["score"]
                    else:
                        raise Exception("Invalid Type Error:" + str(type(value)) + " is not a valid question type")
            elif isinstance(questions, question.Question):
                self.questions[questions.data["Q_id"]] = questions
                self.total_score += questions.data["score"]
            else:
                raise Exception("Invalid Type Error:" + str(type(questions)) + " is not a valid question type")
        except Exception as e:
            print(e)

    def remove_questions(self, question_ids):
        """
        Remove a question from the quiz.
        :param question_ids: ID of the question to be removed.
        :raises Exception: If the question ID does not exist in the quiz.
        :return: None
        """
        try:
            if self.responses:
                raise Exception("Responses Error: Cannot add questions to a quiz with responses")
            if isinstance(question_ids, list):
                for question_id in question_ids:
                    if question_id in self.questions:
                        self.total_score -= self.questions[question_id].data["score"]
                        del self.questions[question_id]
                    else:
                        raise Exception("ID Error: Question ID " + str(question_id) + " does not exist")
            elif isinstance(question_ids, int):
                if question_ids in self.questions:
                    self.total_score -= self.questions[question_ids].data["score"]
                    del self.questions[question_ids]
                else:
                    raise Exception("ID Error: Question ID " + str(question_ids) + " does not exist")
            else:
                raise Exception("Invalid Type Error:" + str(type(question_ids)) + " is not a valid question ID type")
        except Exception as e:
            print(e)

    def add_responses(self, responses = None):
        try:
            if isinstance(responses, Response):
                self.responses[responses.student_id] = responses
            elif isinstance(responses, list):
                for r in responses:
                    if isinstance(r, Response):
                        self.responses[r.student_id] = r
                    else:
                        raise TypeError("Invalid Type Error:" + str(type(r)) + " is not a valid response type")
            elif isinstance(responses, dict):
                for key, value in responses.items():
                    if isinstance(value, Response) and isinstance(key, str):
                        self.responses[key] = value
                    else:
                        raise TypeError("Invalid Type Error:" + str(type(value)) + " is not a valid response type")
            elif responses is None:
                while True:
                    student_id = input("Please enter your student ID: ")
                    if student_id in self.responses:
                        print("You have already taken the quiz.")
                        break
                    elif student_id.isnumeric() is False:
                        print("Please enter a valid student ID.")
                    else:
                        self.take_quiz(student_id)
                        break
            else:
                raise TypeError("Invalid Type Error:" + str(type(responses)) + " is not a valid response type")
        except TypeError as e:
            print(e)

    def take_quiz(self, student_id):
        print(f"Student {student_id}, please answer the following questions:")
        # store the answer list.
        response_list = []
        # access the value that contain the info about each question in the quiz.
        for q in self.questions.values():
            print(q["question"])
            if "notice" in q:
                print(f"note:{q['notice']}")
            if "options" in q:
                print(f"options are {q['options']}")
            answer = input("Your answer: ")
            response_list.append(answer)
        # add the response object to the responses dict.
        self.add_responses(Response(student_id, response_list))

