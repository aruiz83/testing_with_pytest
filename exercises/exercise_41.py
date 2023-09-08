import unittest
from app.count_text_lines import count_lines


# Enter your solution here
class TestCountLines(unittest.TestCase):
    def test_count_lines_of_existing_file(self):
        total_lines = count_lines('section_5/evaluate_41.py')
        self.assertEqual(total_lines, 21)

    def test_count_lines_of_non_existing_file(self):
        with self.assertRaises(FileNotFoundError):
            count_lines('non_existing_script.py')


# Run the tests
if __name__ == '__main__':
    unittest.main()
