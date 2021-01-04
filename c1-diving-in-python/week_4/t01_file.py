"""
В этом задании вам нужно создать интерфейс для работы с файлами.
Класс File должен поддерживать несколько необычных операций.
"""
import os
import tempfile
import uuid


class File:
    """Интерфейс для работы с файлами."""

    def __init__(self, path):
        self.path = path
        self.current_position = 0
        if not os.path.exists(path):
            open(self.path, 'w').close()

    def read(self):
        with open(self.path, 'r') as f:
            return f.read()

    def write(self, to_write):
        with open(self.path, 'w') as f:
            return f.write(to_write)

    def __add__(self, other):
        new_path = os.path.join(tempfile.gettempdir(), str(uuid.uuid4().hex))
        new_file = File(new_path)
        new_file.write(self.read() + other.read())
        return new_file

    def __str__(self):
        return self.path

    def __iter__(self):
        return self

    def __next__(self):
        with open(self.path, 'r') as f:
            f.seek(self.current_position)
            res = f.readline()
            if not res:
                self.current_position = 0
                raise StopIteration('EOF')
            self.current_position += len(res)
            return res


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
