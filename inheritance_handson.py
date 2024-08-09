class Shape:
    def __init__(self, name: str):
        self.name = name


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, length, breadth):
        super().__init__("Rectangle")
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth


class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__("Triangle")
        self.base = base
        self.height = height

    def area(self):
        return .5 * self.height * self.base


my_circle = Circle(5)
my_rectangle = Rectangle(4, 6)
my_triangle = Triangle(3, 8)
print(f"{my_circle.name} and {my_circle.radius}")
print(my_circle.area())
print(my_rectangle.area())
print(my_triangle.area())
