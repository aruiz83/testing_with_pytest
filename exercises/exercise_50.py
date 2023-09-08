import unittest
from app.calculate_salary import calculate_salary


# Enter your solution here
class TestCalculateSalary(unittest.TestCase):
    def test_different_length_lists(self):
        with self.assertRaisesRegex(ValueError, 'Wages and hours lists must have the same length'):
            calculate_salary([1, 2, 3], [1, 2, 3, 4])

    def test_non_numeric_wages(self):
        with self.assertRaisesRegex(TypeError, 'Wages list must contain numbers'):
            calculate_salary(["one", 2, 3], [1, 2, 3])

    def test_non_numeric_hours(self):
        with self.assertRaisesRegex(TypeError, 'Hours list must contain numbers'):
            calculate_salary([1, 2, 3], [1, "2", 3])

    def test_negative_hours(self):
        with self.assertRaisesRegex(ValueError, 'Hours must be non-negative'):
            calculate_salary([1, 2, 3], [1, 2, -3])

    def test_negative_wages(self):
        with self.assertRaisesRegex(ValueError, 'Wages must be non-negative'):
            calculate_salary([-1, 2, 3], [1, 2, 3])

    def test_zero_salary_warning(self):
        with self.assertWarns(UserWarning, msg='Total salary is zero or negative'):
            calculate_salary([10, 20, 30], [0, 0, 0])


# Run the tests
if __name__ == '__main__':
    unittest.main()
