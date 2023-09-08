import unittest
from app.calculator import Calculator


# Enter your solution here
class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_divide_positive_numbers(self):
        self.assertEqual(self.calculator.divide(10, 5), 2)

    def test_divide_zero_by_positive_number(self):
        self.assertEqual(self.calculator.divide(0, 5), 0)

    def test_divide_negative_by_positive_number(self):
        self.assertEqual(self.calculator.divide(-10, 5), -2)

    def test_divide_by_zero_should_raise_error(self):
        with self.assertRaises(ValueError):
            self.calculator.divide(10, 0)

    def tearDown(self) -> None:
        del self.calculator


# Run the tests
if __name__ == '__main__':
    unittest.main()
