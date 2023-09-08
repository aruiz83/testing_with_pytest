import unittest
from app.calculator import Calculator


# Enter your solution here
class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def tearDown(self):
        del self.calculator

    # my solution
    def test_calculator_add(self):
        assert self.calculator.add(1, 2) == 3

    def test_calculator_subtract(self):
        assert self.calculator.subtract(1, 2) == -1

    # excercise solution
    def test_add(self):
        result = self.calculator.add(2, 3)
        self.assertEqual(result, 5)

    def test_subtract(self):
        result = self.calculator.subtract(3, 2)
        self.assertEqual(result, 1)


# Run the tests
if __name__ == '__main__':
    unittest.main()
