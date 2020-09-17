class Car:
    def __init__(self, number_of_door, number_of_wheel):
        self.number_of_door = number_of_door
        self.number_of_wheel = number_of_wheel

    def get_number_of_doors(self):
        return self.number_of_door

    def get_number_of_wheels(self):
        return self.number_of_wheel


my_car = Car(4, 4)
my_car.get_number_of_doors()
my_car.get_number_of_wheels()


