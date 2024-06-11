class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        super().__init__()  
        self.length = length

    def area(self):
        return self.length * self.length
    
class Rectangle(Shape):
    def __init__(self, height, width):
        super().__init__()  
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width

shape = Shape()
print("Shape area:", shape.area())

square = Square(4)
print("Square area:", square.area())

rectangle = Rectangle(4, 5)
print("Rectangle area:", rectangle.area())