class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def move(self):
        print("Move")

class Car(Vehicle):
    pass

class Boat(Vehicle):
    def move(self):
        print("Sail")

class Plane(Vehicle):
    def move(self):
        print("Fly")

b1 = Boat("Yamaha", "242X")
b1.move()

p1 = Plane("Boeing", "747")
p1.move()

c1= Car("Toyota", "Camry")
c1.move()