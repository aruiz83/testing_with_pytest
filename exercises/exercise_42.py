import unittest
from app.calculate_grade import calculate_grade


# Enter your solution here
class TestCalculateGrade(unittest.TestCase):
    def test_valid_input(self):
        self.assertEqual(calculate_grade([1, 2, 3]), 2)
        self.assertEqual(calculate_grade([8, 8, 8]), 8)
        self.assertEqual(calculate_grade([10, 20, 30]), 20)
        self.assertEqual(calculate_grade([11, 22, 33]), 22)
        self.assertEqual(calculate_grade([100, 0, 50]), 50)
        self.assertEqual(calculate_grade([99, 99, 99]), 99)
        self.assertAlmostEqual(
            calculate_grade([100, 90, 80, 70]), 85.0, places=2
        )


# Run the tests
if __name__ == '__main__':
    unittest.main()
