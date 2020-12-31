import os
import tempfile
import json
import argparse

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')


def clear():
    os.remove(storage_path)


def get_data():
    if not os.path.exists(storage_path):
        return {}

    with open(storage_path, 'r') as f:
        raw_data = f.read()
        if raw_data:
            return json.loads(raw_data)
        return {}


def put(key, value):
    data = get_data()
    if key in data:
        data[key].append(value)
    else:
        data[key] = [value]

    with open(storage_path, 'w') as f:
        f.write(json.dumps(data))


def get(key):
    data = get_data()
    return data.get(key)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Key-Value Storage")
    parser.add_argument("-k", "--key", help='Key')
    parser.add_argument("-v", "--val", help='Value')
    parser.add_argument("-c", "--clear", action='store_true', help='Clear')

    args = parser.parse_args()

    if args.clear:
        clear()
    elif args.key and args.val:
        put(args.key, args.val)
    elif args.key:
        if get(args.key) is None:
            print(get(args.key))
        elif len(get(args.key)) >= 1:
            print(', '.join(get(args.key)))
    else:
        print("wrong format!!!")
