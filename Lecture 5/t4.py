import math
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y 
        
    def show(self):
        print(f"Point coordinates: ({self.x}, {self.y})") 
        
    def move(self, x2, y2):
        self.x = x2
        self.y =y2
    def dist(self, x2, y2):
        return math.sqrt((self.x - x2) **2 +(self.y - y2)**2)
    
p1 = Point(1,2)
p2 = Point(4,6)

p1.show()  
p2.show()  

p1.move(3, 4)
p1.show()  

distance = p1.dist(4, 6)
print(f"Distance between points: {distance}")