"""
В этом задании вам нужно создать интерфейс для работы с файлами.
Класс File должен поддерживать несколько необычных операций.
"""
import os
import tempfile


class File:
    def __init__(self, path):
        self.path = path
        self.f = open(path, 'r+')

    def write(self, line):
        with open(self.path, 'a') as f:
            return f.write(line)

    def read(self):
        with open(self.path, 'r') as f:
            return f.read()

    def __str__(self):
        return self.path

    def __iter__(self):
        return self

    def __next__(self):
        line = self.f.readline()
        if line:
            return line
        else:
            raise StopIteration

    def __add__(self, other):
        tmp_path = os.path.join(tempfile.gettempdir(), 'new_file.txt')
        with open(tmp_path, 'w') as f:
            for line in self.f:
                f.write(line)
            for line in other.f:
                f.write(line)
        return File(tmp_path)

    def __del__(self):
        self.f.close()


if __name__ == '__main__':
    filename1 = 'task01_file1.txt'
    filename2 = 'task01_file2.txt'

    # Класс инициализируется полным путем.
    obj = File(filename1)

    # Класс должен поддерживать стандартную функцию print, выводящую путь
    print(obj)

    # Класс должен поддерживать метод write.
    obj.write('line\n')

    # Объекты типа File должны поддерживать протокол итерации
    for line in File(filename1):
        print(line, end='')

    #   Объекты типа File должны поддерживать сложение.
    """
        В этом случае создается новый файл и файловый объект,
        в котором содержимое второго файла добавляется к содержимому первого файла.
        Новый файл должен создаваться в директории, полученной с помощью tempfile.gettempdir.
        Для получения нового пути можно использовать os.path.join.
    """
    print('#################################')
    first = File(filename1)
    second = File(filename2)
    new_obj = first + second
    print('path = ' + str(new_obj))
    for line in new_obj:
        print(line, end='')
