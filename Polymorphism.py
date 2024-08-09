class Vehicle:
    def move(self):
        print("I am a vehicle")


class car(Vehicle):
    def move(self):
        print("Car drives in Road")


class boat(Vehicle):
    def move(self):
        print("Boat moves in water")


#v = Vehicle()
c = car()
c.move()
b = boat()
b.move()

