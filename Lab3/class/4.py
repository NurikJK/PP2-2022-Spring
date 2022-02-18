class Points:
    def __init__(self, x, y):
        self.res = ' '
        self.x = x
        self.y = y
    def show(self):
        print(self.x, self.y)
    def move(self):
        self.x = self.x + step
        self.y = self.y + step
    def dist(self):
        if self.x > self.y:
            self.res = self.x - self.y
        else:
            self.res = self.y - self.x
        print(self.res)
x,y = map(int, input().split())
step = int(input())
p1 = Points(x, y)
p1.show()
p1.move()
print('After moving points to ' + str(step) + ' positions we will get: ', end=' ')
p1.show()
print('Distance between this points: ', end='')
p1.dist()