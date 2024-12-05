import unittest
from Objects.question import Question, MultipleChoice, ShortAnswerQuestion, TrueFalseQuestion  # Replace with your module name

class TestQuestion(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Setting up shared resources for TestQuestion...")
        cls.sample_question = [Question(1, "What is the capital of France?", "Paris", score=5),
                               Question(2, "What is the square root of 16?", "4", score=3),
                               Question(1, "What is the capital of France?", "Paris", score=5)]

    def setUp(self):
        print("Setting up resources for a test case...")
        self.test_question = Question(2, "What is 2 + 2?", "4", score=1)

    def tearDown(self):
        print("Cleaning up after a test case...")
        self.test_question = None

    @classmethod
    def tearDownClass(cls):
        print("Cleaning up shared resources after all tests...")
        cls.sample_question = None

    def test_str_representation(self):
        result = str(self.test_question)
        expected = "ID: 2, Question: What is 2 + 2?, Score: 1"
        self.assertEqual(result, expected)
        self.assertIn("ID: 2", result)
        self.assertIn("Score: 1", result)
        self.assertTrue(isinstance(result, str))

    def test_equality(self):
        another_question = Question(2, "What is 2 + 2?", "4", score=1)
        self.assertEqual(self.test_question, another_question)
        self.assertFalse(self.sample_question[0] == self.sample_question[1])
        self.assertTrue(self.sample_question[0] != self.sample_question[1])
        self.assertTrue(self.sample_question[0] == self.sample_question[2])
        

class TestMultipleChoice(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Setting up shared resources for TestMultipleChoice...")
        cls.sample_question = MultipleChoice(3, "What is the largest planet?", "Jupiter", score=3, options=["Earth", "Mars", "Jupiter", "Venus"])

    def setUp(self):
        print("Setting up resources for a test case...")
        self.test_question = MultipleChoice(4, "What is 5 + 3?", "8", score=1, options=["6", "7", "8", "9"])

    def tearDown(self):
        print("Cleaning up after a test case...")
        self.test_question = None

    @classmethod
    def tearDownClass(cls):
        print("Cleaning up shared resources after all tests...")
        cls.sample_question = None

    def test_str_representation(self):
        result = str(self.test_question)
        self.assertIn("ID: 4", result)
        self.assertIn("Options:", result)
        self.assertIn("8", str(self.test_question.data["options"]))
        self.assertTrue(isinstance(result, str))

    def test_options(self):
        options = self.test_question.data["options"]
        self.assertEqual(len(options), 4)
        self.assertIn("8", options)
        self.assertIn("6", options)
        self.assertIn("7", options)

class TestShortAnswerQuestion(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Setting up shared resources for TestShortAnswerQuestion...")
        cls.sample_question = ShortAnswerQuestion(5, "Define AI.", "Artificial Intelligence", score=5, notice="Please be concise.")

    def setUp(self):
        print("Setting up resources for a test case...")
        self.test_question = [ShortAnswerQuestion(6, "What is DNA?", "Deoxyribonucleic Acid", score=3, notice="Answer in one sentence."),
                              ShortAnswerQuestion(7, "What is Dragon?", "A mythical creature ", score=2, notice="Answer in one sentence.")]

    def tearDown(self):
        print("Cleaning up after a test case...")
        self.test_question = None

    @classmethod
    def tearDownClass(cls):
        print("Cleaning up shared resources after all tests...")
        cls.sample_question = None

    def test_str_representation(self):
        result = str(self.test_question[0])
        self.assertIn("ID: 6", result)
        self.assertIn("Note:", result)
        self.assertIn("Answer in one sentence.", result)
        self.assertTrue(isinstance(result, str))

    def test_notice(self):
        self.assertEqual(self.test_question[0].data["notice"], "Answer in one sentence.")
        self.assertEqual(self.sample_question.data["notice"], "Please be concise.")
        self.assertNotEqual(self.test_question[0].data["score"], self.test_question[1].data["score"])
        self.assertEqual(self.test_question[0].data["score"], 3)

class TestTrueFalseQuestion(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Setting up shared resources for TestTrueFalseQuestion...")
        cls.sample_question = TrueFalseQuestion(7, "The Earth is flat.", "False", score=1)

    def setUp(self):
        print("Setting up resources for a test case...")
        self.test_question = TrueFalseQuestion(8, "Water freezes at 0°C.", "True", score=1)

    def tearDown(self):
        print("Cleaning up after a test case...")
        self.test_question = None

    @classmethod
    def tearDownClass(cls):
        print("Cleaning up shared resources after all tests...")
        cls.sample_question = None

    def test_str_representation(self):
        result = str(self.test_question)
        self.assertIn("ID: 8", result)
        self.assertIn("Options:", result)
        self.assertIn("True", result)
        self.assertIn("False", result)

    def test_correct_answer(self):
        self.assertEqual(self.test_question.data["answer"], "True")
        self.assertIsNotNone(self.test_question.data["options"])
        self.assertEqual(self.test_question.data["options"], ["True", "False"])
        self.assertNotEqual(self.test_question.data["answer"], self.sample_question.data["answer"])

if __name__ == "__main__":
    unittest.main()
