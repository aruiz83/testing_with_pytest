import unittest
import tempfile
from app.file_reader import FileReader


# Enter your solution here

class TestFileReader(unittest.TestCase):
    def setUp(self):
        # self.file_reader = FileReader('file.txt')
        self.file = tempfile.NamedTemporaryFile(mode='w', delete=False)
        self.file.write("Hello, world!")
        self.file.close()

    def tearDown(self):
        # del self.file_reader
        # Delete the temporary file
        import os
        os.unlink(self.file.name)

    def test_read_file(self):

        # value = self.file_reader.read_file('file.txt')
        # self.assertEqual(value, "Hello, world!")
        reader = FileReader()
        # Read the contents of the test file using the read_file method
        result = reader.read_file(self.file.name)
        # Check that the contents of the file match the expected value
        self.assertEqual(result, "Hello, world!")


# Run the tests
if __name__ == '__main__':
    unittest.main()
