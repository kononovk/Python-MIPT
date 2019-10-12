class File:
    def __init__(self, path):
        self.path = path
        self.f = open(path, 'w+')


    def __str__(self):
        return self.path

    def write(self, line):
        self.f.write(line)


"""
В этом задании вам нужно создать интерфейс для работы с файлами.
Класс File должен поддерживать несколько необычных операций.
"""
if __name__ == '__main__':
    obj = File('task01.txt')   # Класс инициализируется полным путем.
    obj.write('line\n')           # Класс должен поддерживать метод write.

    #   Объекты типа File должны поддерживать сложение.
    """
        В этом случае создается новый файл и файловый объект,
        в котором содержимое второго файла добавляется к содержимому первого файла.
        Новый файл должен создаваться в директории, полученной с помощью tempfile.gettempdir.
        Для получения нового пути можно использовать os.path.join.
    """
    # first = File('/tmp/first')
    # second = File('/tmp/second')
    # new_obj = first + second
