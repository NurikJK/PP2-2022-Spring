class Shape:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        print("Default area: 0")
class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__(length, width)
    def area(self):
        print(self.length * self.width)

x = int(input())
y = int(input())
sh = Shape(x, y)
sh.area()
sq = Rectangle(x, y)
sq.area()
