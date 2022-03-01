def sequence(x,d):
    d = int(d ** 0.5)
    x = int(x ** 0.5)
    while x <= d:
        yield x * x
        x += 1

for i in sequence(int(input()),int(input())):
    print(i,end = " ")