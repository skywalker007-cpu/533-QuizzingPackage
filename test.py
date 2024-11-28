import unittest
from quiz import Quiz
import question

class TestQuiz(unittest.TestCase):
    def setUp(self):
        self.Q1 = question.MultipleChoice(1, "What is the capital of France?", "Paris", 1,
                                        ["Paris", "London", "Berlin", "Madrid"])
        self.Q2 = question.ShortAnswerQuestion(2, "What is the capital of France?", "Paris", 1, "Please answer in one word")
        self.Q3 = question.TrueFalseQuestion(3, "Is Paris the capital of France?", "True", 1, ["True", "False"])
        self.Q4 = question.MultipleChoice(4, "What is the capital of Germany?", "Berlin", 1,
                                        ["Paris", "London", "Berlin", "Madrid"])
        self.Q5 = question.ShortAnswerQuestion(5, "What is the capital of Germany?", "Berlin", 1, "Please answer in one word")
        self.Q6 = question.TrueFalseQuestion(6, "Is Berlin the capital of Germany?", "True", 1, ["True", "False"])
        
        self.quiz_1 = Quiz()
        
        self.quiz_1.add_questions(self.Q1)
        self.quiz_1.add_questions(self.Q2)
        self.quiz_1.add_questions(self.Q3)
        
        self.quiz_2 = Quiz()
        
        self.quiz_2.add_questions(self.Q4)
        self.quiz_2.add_questions(self.Q5)
        self.quiz_2.add_questions(self.Q6)
        
        self.quiz_3 = self.quiz_1.clone()
        
    def test_clone(self):
        self.assertEqual(self.quiz_1, self.quiz_3)
        self.assertNotEqual(self.quiz_1, self.quiz_2)
    
    
unittest.main(argv=[''], exit=False)
