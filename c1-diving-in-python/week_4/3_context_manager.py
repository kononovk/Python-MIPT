import time


class timer:
    def __init__(self):
        self.start = time.time()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Summary time: {:.3f}'.format(self.current_time()))

    def current_time(self):
        return time.time() - self.start


if __name__ == '__main__':
    with timer() as t:
        time.sleep(0.5)
        print('Current: {:.3f}'.format(t.current_time()))
        time.sleep(0.5)
        type
