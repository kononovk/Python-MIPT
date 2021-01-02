import functools
import json


def to_json(func):
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        result = func(*args, **kwargs)
        return json.dumps(result)

    return wrapped


@to_json
def get_data1():
    return {'data': 42, 'data2': 3, 'data3': 42}


@to_json
def get_data2():
    return [1, 2, 3]


@to_json
def get_data3(a, b):
    return a, b


if __name__ == '__main__':
    # get_data -> to_json(get_data())
    print(get_data1())
    print(get_data2())
    print(get_data3(1, 2))
