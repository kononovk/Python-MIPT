class Value:
    def __init__(self):
        self.val = None

    def __get__(self, obj, obj_type):
        return self.val

    def __set__(self, obj, value):
        self.val = value * (1 - obj.commission)


class Account:
    amount = Value()

    def __init__(self, commission):
        self.commission = commission


if __name__ == '__main__':
    new_account = Account(0.1)
    new_account.amount = 100
    print(new_account.amount)
