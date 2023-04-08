from abc import ABC, abstractmethod


class Transport(ABC):
    """ 1 Шаг. Создание абстрактного класса Transport"""
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def stop(self):
        pass

""" 2 Шаг. Добавление классов Boat, Car, Electroscooter, которые наследуются от абстрактного класса Transport """
class Boat(Transport):
    def start_engine(self):
        print('Двигатель катера запущен')

    def stop_engine(self):
        print('Двигатель катера остановлен')

    def move(self):
        print('Катер движется')

    def stop(self):
        print('Катер остановился')

class Car(Transport):
    def start_engine(self):
        print('Двигатель машины запущен')

    def stop_engine(self):
        print('Двигатель машины остановлен')

    def move(self):
        print('Машина движется')

    def stop(self):
        print('Машина остановилась')

class Electroscooter(Transport):
    def start_engine(self):
        print('Двигатель электро скутера запущен')

    def stop_engine(self):
        print('Двигатель электро скутера остановлен')

    def move(self):
        print('Электро скутер движется')

    def stop(self):
        print('Электро скутер остановился')

""" 3 Шаг. Добавление класса Person """
class Person:
    @staticmethod
    def use_transport(transport: Transport):
        transport.start_engine()
        transport.move()
        transport.stop_engine()
        transport.stop()


if __name__ == '__main__':
    boat = Boat()
    car = Car()
    kamikadze = Electroscooter()

    person = Person()
    person.use_transport(boat)
    print('=' * 10)
    person.use_transport(car)
    print('=' * 10)
    person.use_transport(kamikadze)
