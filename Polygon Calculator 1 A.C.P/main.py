class Polygon:
    def calculate_area(self):
        pass

class Rectangle(Polygon):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

class Square(Polygon):
    def __init__(self, side_length):
        self.side_length = side_length

    def calculate_area(self):
        return self.side_length * self.side_length

class Triangle(Polygon):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height

if __name__ == "__main__":
    rectangle = Rectangle(5, 10)
    square = Square(6)
    triangle = Triangle(8, 4)

    print("Rectangle Area:", rectangle.calculate_area())
    print("Square Area:", square.calculate_area())
    print("Triangle Area:", triangle.calculate_area())
