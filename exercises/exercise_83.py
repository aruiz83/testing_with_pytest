import unittest
from app.emp import Employee


class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.emp = Employee('John', 'Smith', 40, 80000)

    def test_email(self):
        self.assertEqual(self.emp.email, 'john.smith@mail.com')


# Run the tests
if __name__ == '__main__':
    unittest.main()
