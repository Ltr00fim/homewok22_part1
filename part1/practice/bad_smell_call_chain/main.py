class Person:
    def __init__(self, city: int, room_number: int):
        self._city = city
        self._room_number = room_number

    def get_person_room(self):
        return self._room_number

    def get_city_population(self):
        return self._city


if __name__ == '__main__':
    person = Person(10, 20)
    print(person.get_person_room())
    print(person.get_city_population())