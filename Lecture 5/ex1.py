class Car():
    color = 'black'
    brand = 'Tesla'
    engine = 'electiricity'
    # def __init__(self, color, brand, engine) -> None:
    #     self.color = color
    #     self.brand = brand
    #     self.engine = engine
        
        
# c1 = Car('red', 'Tesla', 'electricity')
# c2 = Car('black', 'BMW', 'fuel')
c1 = Car()
c1.brand = 'BMW'
c2 = Car()
print(Car.__dict__)
print(c1.__dict__)
print(c2.__dict__)
delattr(c1, 'brand')
print(c1.__dict__)
print(c1.brand)