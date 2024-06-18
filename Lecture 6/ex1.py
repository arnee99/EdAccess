# Functional programming
# OOP

# func1() -> task1
# func2() -> task2
# func3() -> task3
# func4() -> task4

# Large amount of code
# Slow
# Some memory loss

# OOP -> Object Oriented Programming
# Object -> instance of Class
# instance (экземпляр)
# ATM -> банкомат
# Class Deposit -> DepositID, DepositOwnerID, DepositOwnerName
# Class Credit -> CreditID, CreditOwnerID, CreditOwnerName
# Class User -> UserID, UserName, UserIIN, trustworthiness
# Class Withdrawal -> WithdrawalID, WithdrawalSum, WithdrawalTime

# 10,000 ATMS

class Shape():
    # initial list of parameters
    # name = "Intial Shape"
    # sideNumber = 3
    # area = 0
    # color = "White"
    
    # initial list of functions
    # init -> initialize
    # Set values for parameters
    # __init__() -> is called when the new object is created
    def __init__(self, name, sideNumber, area, color):
        self.name = name
        self.sideNumber = sideNumber
        self.area = area
        self.color = color
    
    def printName(self):
        print(self)
        print(self.name)
    
    def printArea(self):
        print(self)
        print(self.area)
        
# self -> сам? самостоятельно?

# Inheritance, Polymorphism, Encapsulation, Abstraction (optional)
# Super Class -> Parent Class
# Sub Class -> Child Class

class Rectangle(Shape):
    def __init__(self, name, sideNumber, area, color, isRectangle):
        super().__init__(name, sideNumber, area, color)
        self.isRectangle = isRectangle
    
rect1 = Rectangle("Rectangle", 4, 20, "Blue", True)
rect1.printName()
rect1.printArea()
    
print(Shape.__dict__)      
        
shape1 = Shape("Rectangle", 4, 20, "Blue")
shape2 = Shape("Triangle", 3, 12, "Red")
# shape1.name = "Triangle"
# shape1.color = "Red"
# shape1.area = 15
print(shape1.__dict__)
print(shape2.__dict__)
print(shape1.area, shape1.color, shape1.name)
print(shape2.area, shape2.color, shape2.name)
# shape1.printName()
# shape2.printName()
# shape1.printArea()
# shape2.printArea()