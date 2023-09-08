
class FileReader:
    def read_file(self, filename):
        with open(filename, 'r') as f:
            return f.read()
