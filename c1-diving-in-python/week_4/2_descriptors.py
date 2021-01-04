class SaveToFileDescriptor:
    def __init__(self, value=None):
        self.val = value

    def __get__(self, obj, obj_type):
        return self.val

    def __set__(self, obj, value):
        with open('file.txt', 'a') as f:
            f.write(str(value) + '\n')
        self.val = value

    def __str__(self):
        return str(self.val)


class Class:
    attr = SaveToFileDescriptor()


if __name__ == '__main__':
    instance = Class()
    instance.attr = 5
    print(instance.attr)
