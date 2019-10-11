import csv


class BaseCar:
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand  # brand
        self.photo_file_name = photo_file_name  # ex: "machine.jpg"
        self.carrying = carrying  # gruzopodyemnost

    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[1]


class Truck(BaseCar):
    car_type = 'truck'

    def __init__(self, brand, photo_file_name, carrying, characteristics):
        super(Truck, self).__init__(brand, photo_file_name, carrying)
        if len(characteristics) == 0:
            self.body_length, self.body_width, self.body_height = 0.0, 0.0, 0.0
        else:
            lst = [float(x) for x in s.split('x')]
            lst += [0] * (3 - len(lst))
            [body_length, body_width, body_height] = lst
            self.body_length = body_length
            self.body_width = body_width
            self.body_height = body_height


def get_body_volume(self):
    return self.body_height * self.body_width * self.body_length


class Car(BaseCar):
    car_type = 'car'

    def __init__(self, brand, photo_file_name, carrying, passengers_seats):
        self.passengers_seats = passengers_seats
        super(Car, self).__init__(brand, photo_file_name, carrying)


class SpecMachine(BaseCar):
    car_type = 'spec_machine'

    def __init__(self, brand, photo_file_name, carrying, extra):
        super(Car, self).__init__(brand, photo_file_name, carrying)
        self.extra = extra


def get_car_list(csv_filename):
    car_list = []
    return car_list