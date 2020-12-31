class FileReader:
    """Класс FileReader помогает читать из файла"""
    def __init__(self, filepath):
        self.filepath = filepath
    def read(self):
        try:
            with open(self.filepath, 'r') as f:
                return f.read()
        except IOError:
            return ""

if __name__ == '__main__':
    reader = FileReader("example.txt")
    print(reader.read())
