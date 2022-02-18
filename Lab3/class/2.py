class Shape:
    def __init__(self,length):
        self.length = length
    def area(self):
        print(0)

class Square(Shape):
    def __init__(self, length):
        self.length = length
    def area(self):
        print(self.length * self.length)

s = Shape(7)
s.area()
t = Square(9)
t.area()