import functools
import json


def to_json(func):
    @functools.wraps(func)
    def wraped(*args, **kwargs):
        result = func(*args, **kwargs)
        return json.dumps(result)

    return wraped


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
    print(get_data1())
    print(get_data2())
    print(get_data3(1, 2))

# get_data -> to_json(get_data())
