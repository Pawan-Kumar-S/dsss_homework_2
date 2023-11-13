import unittest
from math_quiz import generate_random_integer, generate_random_operator, arithmetic_operation

class TestMathGame(unittest.TestCase):

    def test_generate_random_integer(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = generate_random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_generate_random_operator(self):
        # Test if the returned operator is one of the expected operators
        operators = {'+', '-', '*'}
        for _ in range(1000):  # Test a large number of random values
            rand_operator = fungenerate_random_operatorction_B()
            self.assertIn(rand_operator, operators)

    def test_arithmetic_operation(self):
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (8, 4, '-', '8 - 4', 4),
            (3, 6, '*', '3 * 6', 18),
            # Add more test cases as needed
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            generated_problem, generated_answer = arithmetic_operation(num1, num2, operator)

            # Test if the generated problem matches the expected problem
            self.assertEqual(generated_problem, expected_problem)

            # Test if the generated answer matches the expected answer
            self.assertEqual(generated_answer, expected_answer)

if __name__ == "__main__":
    unittest.main()
