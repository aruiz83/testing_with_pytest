import unittest

from app.generate_password import generate_password

# Enter your solution here


class TestGeneratePassword(unittest.TestCase):
    def test_generate_password(self):
        result = generate_password(10)
        self.assertEqual(len(result), 10)
        self.assertTrue(any(c.isupper() for c in result))
        self.assertTrue(any(c.islower() for c in result))
        self.assertTrue(any(c.isdigit() for c in result))


# Run the tests
if __name__ == '__main__':
    unittest.main()
