import time


class PascalList:
    def __init__(self, original_list):
        self.container = original_list or []

    def __getitem__(self, item):
        return self.container[item - 1]

    def __setitem__(self, index, value):
        self.container[index - 1] = value

    def __str__(self):
        return self.container.__str__()


class SquareIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration

        result = self.current ** 2
        self.current += 1
        return result


class timer:
    def __init__(self):
        self.start = time.time()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Elapsed {}'.format(self.current_time()))

    def current_time(self):
        return time.time() - self.start


if __name__ == '__main__':
    print("Example1:_____________________________")
    numbers = PascalList(range(10))
    print(numbers[0])  # 9
    print(numbers[1])  # 0
    print(numbers[5])  # 4
    print('Example2:_____________________________')
    for num in SquareIterator(1, 5):
        print(num)
    print("Example3:_____________________________")
    with timer() as t:
        print(t.current_time())
        time.sleep(5)
        print(t.current_time())
