import unittest
from app.rectangle import area, perimeter


class TestArea(unittest.TestCase):
    def test_area(self):
        test_cases = [
            (1, 5, 5),
            (2, 10, 20),
            (100, 50, 5000)
        ]
        for width, height, expected in test_cases:
            with self.subTest(
                width=width, height=height, expected=expected
            ):
                self.assertEqual(area(width, height), expected)


# Run the tests
if __name__ == '__main__':
    unittest.main()
