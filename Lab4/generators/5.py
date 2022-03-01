def fn(n):
    while n > 0:
        yield n
        n -= 1
for i in fn(int(input())):
    print(i,end = ' ')