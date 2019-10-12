import csv
import os


class BaseCar:
    """Базовый класс с общими методами и атрибутами"""

    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand  # brand
        self.photo_file_name = photo_file_name  # ex: "machine.jpg"
        self.carrying = carrying  # gruzopodyemnost

    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[1]

    def __str__(self):
        return '{} / {} / {}'.format(self.brand, self.photo_file_name, self.carrying)


class Truck(BaseCar):
    """Класс грузовой автомобиль"""
    car_type = 'truck'

    def __init__(self, brand, photo_file_name, characteristics, carrying):
        super(Truck, self).__init__(brand, photo_file_name, carrying)
        if len(characteristics) == 0:
            self.body_length, self.body_width, self.body_height = 0.0, 0.0, 0.0
        else:
            lst = [float(x) for x in characteristics.split('x')]
            lst += [0] * (3 - len(lst))
            [body_length, body_width, body_height] = lst
            self.body_length = body_length
            self.body_width = body_width
            self.body_height = body_height

    def __str__(self):
        return super(Truck, self).__str__(self) #+ \
            #str(self.body_height) + 'x' + str(self.body_width) + 'x' + str(self.body_length)

    def get_body_volume(self):
        return self.body_height * self.body_width * self.body_length


class Car(BaseCar):
    """Класс легковой автомобиль"""
    car_type = 'car'

    def __init__(self, brand, passenger_seats_count, photo_file_name, carrying):
        self.passenger_seats_count = passenger_seats_count
        super(Car, self).__init__(brand, photo_file_name, carrying)


class SpecMachine(BaseCar):
    """Класс спецтехника"""
    car_type = 'spec_machine'

    def __init__(self, brand, photo_file_name, carrying, extra):
        super(SpecMachine, self).__init__(brand, photo_file_name, carrying)
        self.extra = extra


def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # пропускаем заголовок
        for row in reader:
            if (len(row) < 7):
                continue
            if row[0] == 'car':
                car = Car(row[1], int(row[2]), row[3], float(row[5]))
            elif row[0] == 'truck':
                car = Truck(row[1], row[3], row[4], float(row[5]))
            elif row[0] == 'spec_machine':
                car = SpecMachine(row[1], row[3], float(row[5]), row[6])
            else:
                continue
            car_list.append(car)
    return car_list


if __name__ == '__main__':
    # print(get_car_list('coursera_week3_cars.csv'))
    machine = Truck("Nissan", "nissan.jpg", '123x123x123', 500)
    print(machine)

