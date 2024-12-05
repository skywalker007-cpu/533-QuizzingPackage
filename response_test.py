import unittest
from Objects import response

class TestResponse(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Runs once before all test cases in this class
        print("Setting up shared resources for TestResponse...")
        cls.shared_responses = [
            response.Response(101, ['A', 'B', 'C']),
            response.Response(102, ['B', 'C', 'D']),
        ]

    def setUp(self):
        # Runs before every test case
        self.test_response = response.Response(103, ['C', 'D', 'A'])

    def tearDown(self):
        # Runs after every test case
        self.test_response = None

    @classmethod
    def tearDownClass(cls):
        # Runs once after all test cases in this class
        print("Cleaning up shared resources after all tests...")
        cls.shared_responses = None


    def test_init_function(self):
        # Test for __init__ method
        self.assertEqual(self.test_response.student_id, 103)
        self.assertEqual(self.test_response.response, ['C', 'D', 'A'])
        self.assertTrue(isinstance(self.test_response.student_id, int))
        # want to check if two response object with different attribute is the same
        self.assertNotEqual(self.test_response.student_id, self.shared_responses[0].student_id)
        self.assertNotEqual(self.test_response.response, self.shared_responses[0].response)

    def test_str_representation(self):
        # Test for __str__ method
        result = str(self.test_response)
        expected = "Student ID: 103, Responses to the quiz: ['C', 'D', 'A']"
        self.assertEqual(result, expected)
        self.assertIn("Student ID: 103", result)
        self.assertIn("['C', 'D', 'A']", result)
        self.assertTrue(isinstance(result, str))

    def test_repr_representation(self):
        # Test for __repr__ method
        result = repr(self.test_response)
        expected = "Dictionary format: Response(key = 103, values = ['C', 'D', 'A'])"
        self.assertEqual(result, expected)
        self.assertIn("key = 103", result)
        self.assertIn("values = ['C', 'D', 'A']", result)
        self.assertTrue(isinstance(result, str))

if __name__ == "__main__":
    unittest.main()
