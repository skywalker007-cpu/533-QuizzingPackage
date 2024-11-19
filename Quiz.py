import Question

class Quiz():
    def __init__(self, questions = None, responses = {}, API_KEY = None):
        self.total_score = 0
        
        self.questions = {}
        if questions is not None:
            self.add(questions)
        self.responses = responses
        self.API_KEY = API_KEY
    def __str__(self):
        return f"\n\nTotal_Score: {self.total_score} \n\nAPI_KEY: {self.API_KEY} \n\nQuestions: {self.questions} \n\nResponses: {self.responses}"
    def add(self, questions = None):
        """
        Add a question or a list of questions to the quiz.
        :param questions: Question or list of questions to be added to the quiz.
        :raises Exception: If the question is not a valid question type.
        :raises Exception: If the question ID already exists in the quiz.
        :return: None
        """
        try:
            if isinstance(questions, list):
                for question in questions:
                    if isinstance(question, Question.Question):
                        if question.data["Q_id"] in self.questions:
                            raise Exception("Duplicate ID Error: Question ID " + str(question.data["Q_id"]) + " already exists")
                        self.questions[question.data["Q_id"]] = question
                        self.total_score += question.data["score"]
                    else:
                        raise Exception("Invalid Type Error:" + str(type(question)) + " is not a valid question type")
            elif isinstance(questions, dict):
                for key, value in questions.items():
                    if isinstance(value, Question.Question):
                        if value.data["Q_id"] in self.questions:
                            raise Exception("Duplicate ID Error: Question ID " + str(value.data["Q_id"]) + " already exists")
                        if value.data["Q_id"] != key:
                            raise Exception("ID Mismatch Error: Question ID " + str(value.data["Q_id"]) + " does not match the key " + str(key))
                        self.questions[value.data["Q_id"]] = value
                        self.total_score += value.data["score"]
                    else:
                        raise Exception("Invalid Type Error:" + str(type(value)) + " is not a valid question type")
            elif isinstance(questions, Question.Question):
                self.questions[questions.data["Q_id"]] = questions
                self.total_score += questions.data["score"]     
            else:
                raise Exception("Invalid Type Error:" + str(type(questions)) + " is not a valid question type")
        except Exception as e:
            print(e)
    def remove(self, question_ids):
        """
        Remove a question from the quiz.
        :param question_id: ID of the question to be removed.
        :raises Exception: If the question ID does not exist in the quiz.
        :return: None
        """
        try:
            if isinstance(question_ids, list):
                for question_id in question_ids:
                    if question_id in self.questions:
                        del self.questions[question_id]
                    else:
                        raise Exception("ID Error: Question ID " + str(question_id) + " does not exist")
            elif isinstance(question_ids, int):
                if question_ids in self.questions:
                    del self.questions[question_ids]
                else:
                    raise Exception("ID Error: Question ID " + str(question_ids) + " does not exist")
            else:
                raise Exception("Invalid Type Error:" + str(type(question_ids)) + " is not a valid question ID type")
        except Exception as e:
            print(e)
    def clone(self):
        """
        Clone the quiz object.
        :return: Quiz object
        """
        return Quiz(self.questions, {}, self.API_KEY)