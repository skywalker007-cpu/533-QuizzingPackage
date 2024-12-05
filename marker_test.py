import unittest
from Quizzes.quiz import Quiz
import Objects.question as question
from Objects.response import Response
from unittest.mock import patch
from io import StringIO
from Quizzes.marker import Marker

class TestMarker(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.Q1 = question.MultipleChoice(1, "What is the capital of France?", "Paris", 1,
                                        ["Paris", "London", "Berlin", "Madrid"])
        cls.Q2 = question.ShortAnswerQuestion(2, "What is the capital of France?", "Paris", 1, "Please answer in one word")
        cls.Q3 = question.TrueFalseQuestion(3, "Is Paris the capital of France?", "True", 1, ["True", "False"])
        cls.Q4 = question.MultipleChoice(4, "What is the capital of Germany?", "Berlin", 1,
                                        ["Paris", "London", "Berlin", "Madrid"])
        cls.Q5 = question.ShortAnswerQuestion(5, "What is the capital of Germany?", "Berlin", 1, "Please answer in one word")
        cls.Q6 = question.TrueFalseQuestion(6, "Is Berlin the capital of Germany?", "True", 1, ["True", "False"])
    
        cls.correct_response_1 = Response("001", ["Paris", "Paris", "True"])
        cls.correct_response_2 = Response("002", ["Paris", "Paris", "True"])
        cls.correct_response_3 = Response("003", ["Paris", "Paris", "True"])
        cls.incorrect_response_1 = Response("004", ["Paris", "Paris", "False"])
        cls.incorrect_response_2 = Response("005", ["Paris", "Paris", "False"])
        cls.incorrect_response_3 = Response("006", ["Paris", "Paris", "False"])
        
        cls.marker = Marker()
        
    @classmethod
    def tearDownClass(cls):
        return super().tearDownClass()
    
    def setUp(self):
        self.quiz_1 = Quiz()
        
        self.quiz_1.add_questions(self.Q1)
        self.quiz_1.add_questions(self.Q2)
        self.quiz_1.add_questions(self.Q3)
        
        self.quiz_2 = Quiz()
        
        self.quiz_2.add_questions(self.Q4)
        self.quiz_2.add_questions(self.Q5)
        self.quiz_2.add_questions(self.Q6)
        
        self.quiz_3 = self.quiz_1.clone()
        self.quiz_for_editing = Quiz()
             
    def tearDown(self) -> None:
        return super().tearDown()

    def test_marking(self):
        self.quiz_1.add_responses({"001" : Response("001", ["Paris", "Paris", "True", "False"])})
        self.quiz_1.mark_quiz()
        self.assertEqual(self.quiz_1.marks, {"001" : 0})
        
        self.quiz_1.add_responses({"001" : Response("001", ["Paris", "Paris", "True"])})
        self.quiz_1.mark_quiz()
        self.assertEqual(self.quiz_1.marks, {"001" : 3})
        
        self.quiz_2.add_responses({"001" : Response("001", ["Paris", "Paris", "True"])})
        self.quiz_2.add_responses({"002" : Response("002", ["Paris", "Paris", "False"])})
        self.quiz_2.mark_quiz()
        self.assertEqual(self.quiz_2.marks, {"001" : 1, "002" : 0})
        
        self.quiz_2.add_responses({"001" : Response("001", ["Paris", "", "False"])})
        self.quiz_2.mark_quiz()
        self.assertEqual(self.quiz_2.marks, {"001" : 0, "002" : 0})
        
    @patch('sys.stdout', new_callable=StringIO)
    def test_marking_exceptions(self, mock_stdout):
        self.quiz_1.add_responses({"001" : Response("001", ["Paris", "Paris", "True", "False"])})
        self.quiz_1.mark_quiz()
        self.marker.mark(self.quiz_1.questions, "response")
                
        self.assertEqual(
            mock_stdout.getvalue().strip(),
            "The number of responses does not match the number of questions in the quiz.\nThe response is not a valid list."
        )


        
        
        
        
        
        
unittest.main(argv=[''], exit=False)