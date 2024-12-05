import unittest
from response_test import TestResponse
from question_test import TestQuestion, TestMultipleChoice, TestTrueFalseQuestion, TestShortAnswerQuestion
from quiz_test import TestQuiz
from marker_test import TestMarker

def my_suite():
    suite = unittest.TestSuite()
    result = unittest.TestResult()
    suite.addTest(TestResponse('test_init_function'))
    suite.addTest(TestResponse('test_str_representation'))
    suite.addTest(TestResponse('test_repr_representation'))
    suite.addTest(TestQuestion('test_str_representation'))
    suite.addTest(TestQuestion('test_equality'))
    suite.addTest(TestMultipleChoice('test_str_representation'))
    suite.addTest(TestMultipleChoice('test_options'))
    suite.addTest(TestShortAnswerQuestion('test_str_representation'))
    suite.addTest(TestShortAnswerQuestion('test_notice'))
    suite.addTest(TestTrueFalseQuestion('test_str_representation'))
    suite.addTest(TestTrueFalseQuestion('test_correct_answer'))
    suite.addTest(TestQuiz('test_clone'))
    suite.addTest(TestQuiz('test_add_and_remove_questions'))
    suite.addTest(TestQuiz('test_responses'))
    suite.addTest(TestQuiz('test_marking'))
    suite.addTest(TestMarker('test_marking'))
    suite.addTest(TestMarker('test_marking_exceptions'))
    runner = unittest.TextTestRunner()
    print(runner.run(suite))
my_suite()