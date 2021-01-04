import os
import csv


class CarBase:
    """базовый класс для всех типов машин"""

    def __init__(self, car_type, photo_file_name, brand, carrying):
        assert brand and car_type and photo_file_name
        self.car_type = car_type  # тип машины ("car", "truck", "spec_machine")
        self.photo_file_name = photo_file_name  # имя файла с изображением машины
        if self.get_photo_file_ext() not in {'.jpg', '.jpeg', '.png', '.gif'}:
            raise ValueError
        self.brand = brand  # марка производителя машины
        self.carrying = float(carrying)  # грузоподъемность

    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[1]


class Car(CarBase):
    """легковые автомобили"""

    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__("car", photo_file_name, brand, carrying)
        self.passenger_seats_count = int(passenger_seats_count)


class Truck(CarBase):
    """грузовой автомобиль"""

    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__("truck", photo_file_name, brand, carrying)
        try:
            self.body_length, self.body_width, self.body_height = map(float, body_whl.split('x'))
        except:
            self.body_length, self.body_width, self.body_height = 0., 0., 0.

    def get_body_volume(self):
        return self.body_height * self.body_width * self.body_length


class SpecMachine(CarBase):
    """специальные автомобили"""

    def __init__(self, brand, photo_file_name, carrying, extra):
        assert extra
        super().__init__("spec_machine", photo_file_name, brand, carrying)
        self.extra = extra


def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename, 'r') as f:
        reader = csv.reader(f, delimiter=';')
        next(reader)
        for row in reader:
            try:
                if row[0] == 'car':
                    car_list.append(Car(brand=row[1], photo_file_name=row[3], carrying=row[5],
                                        passenger_seats_count=row[2]))
                elif row[0] == 'truck':
                    car_list.append(Truck(brand=row[1], photo_file_name=row[3], carrying=row[5],
                                          body_whl=row[4]))
                elif row[0] == 'spec_machine':
                    car_list.append(SpecMachine(brand=row[1], photo_file_name=row[3], carrying=row[5],
                                                extra=row[6]))
            except (ValueError, IndexError, AssertionError):
                continue

        return car_list


if __name__ == '__main__':
    get_car_list('coursera_week3_cars.csv')
