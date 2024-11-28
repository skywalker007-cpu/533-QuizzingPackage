import unittest
from Quizzes.quiz import Quiz
import Questions.question as question

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
        self.quiz_for_editing = Quiz()
        
    def test_clone(self):
        self.assertEqual(self.quiz_1, self.quiz_3)
        self.assertNotEqual(self.quiz_1, self.quiz_2)
    
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
        
unittest.main(argv=[''], exit=False)
