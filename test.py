import unittest
from Quizzes.quiz import Quiz
import Objects.question as question
from Objects.response import Response

class TestQuiz(unittest.TestCase):
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
        
        self.correct_response_1 = Response("001", ["Paris", "Paris", "True"])
        self.correct_response_2 = Response("002", ["Paris", "Paris", "True"])
        self.correct_response_3 = Response("003", ["Paris", "Paris", "True"])
        self.incorrect_response_1 = Response("004", ["Paris", "Paris", "False"])
        self.incorrect_response_2 = Response("005", ["Paris", "Paris", "False"])
        self.incorrect_response_3 = Response("006", ["Paris", "Paris", "False"])
        
    def test_clone(self):
        self.assertEqual(self.quiz_1, self.quiz_3)
        self.assertNotEqual(self.quiz_1, self.quiz_2)
        
        quiz_2_clone_1 = self.quiz_2.clone()
        quiz_2_clone_2 = self.quiz_2.clone()
        self.assertEqual(quiz_2_clone_1, quiz_2_clone_2)
        
        quiz_2_clone_1.add_questions(self.Q1)
        self.assertNotEqual(quiz_2_clone_1, quiz_2_clone_2)
        
        quiz_2_clone_1.remove_questions(1)
        self.assertEqual(quiz_2_clone_1, quiz_2_clone_2)
    
    def test_add_and_remove_questions(self):
        self.quiz_for_editing.add_questions(self.Q4)
        self.quiz_for_editing.add_questions(self.Q5)
        self.quiz_for_editing.add_questions(self.Q6)
        self.assertEqual(self.quiz_2, self.quiz_for_editing)
        self.assertNotEqual(self.quiz_1, self.quiz_for_editing)
        
        self.quiz_for_editing.add_questions({1 : self.Q1})
        self.quiz_for_editing.add_questions({2 : self.Q2})
        self.quiz_for_editing.add_questions({3 : self.Q3})
        self.quiz_for_editing.remove_questions(4)
        self.quiz_for_editing.remove_questions(5)
        self.quiz_for_editing.remove_questions(6)    
        self.assertEqual(self.quiz_1, self.quiz_for_editing)
        self.assertNotEqual(self.quiz_2, self.quiz_for_editing)
        
        self.quiz_for_editing.remove_questions([1,2,3])
        self.assertEqual(0, len(self.quiz_for_editing.questions))
          
    def test_responses(self):
        self.quiz_1.add_responses({"001" : Response("001", ["Paris", "Paris", "True"])})
        self.quiz_1.add_responses({"002" : Response("002", ["Paris", "Paris", "True"])})
        self.quiz_1.add_responses({"003" : Response("003", ["Paris", "Paris", "True"])})
        self.assertEqual(3, len(self.quiz_1.responses))
       
    def test(self):
        return 

unittest.main(argv=[''], exit=False)
