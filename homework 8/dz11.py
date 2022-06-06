import time


class Auto:
    def __init__(self, brand: str, age: int, mark: str, color = 'red', weight = 2000):
        self.brand = brand
        self.age = age
        self.course = mark
        self.cоlor = color
        self.weight= weight

    def birthday(self):
        self.age += 1
        return self.age

    @staticmethod
    def move():
        print('move')

    @staticmethod
    def stop():
        print('stop')


class Truck(Auto):
    def __init__(self, brand: str, age: int, mark: str, max_load: int, color: str = "", weight: float = 0.0):
        super().__init__(brand, age, mark, color, weight)
        self.max_load = max_load

    @staticmethod
    def move():
        print('attention')
        super().move()

    @staticmethod
    def load():
        time.sleep(1)
        print("load")
        time.sleep(1)


class Car(Auto):
    def __init__(self, brand: str, age: int, mark: str, max_speed: int, color: str = "", weight: float = 0.0):
        super().__init__(brand, age, mark, color, weight)
        self.max_speed = max_speed

    def move(self):
        super().move()
        print("max speed is " + str(self.max_speed))


a = Auto("cheurolet", 30, "cruze")

b = Truck('Volvo', 30, 'Fura', 2000, 'red', 20000)
c = Car('Chevrolet', 11, 'cruze', 220)
a.stop()
a.move()
b.move()
c.move()
