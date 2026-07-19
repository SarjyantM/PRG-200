class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} vehicle is starting.")

class Car(Vehicle):
    def honk(self):
        print(f"{self.brand} car goes Beep!")

car = Car("Toyota")
car.start()
car.honk()