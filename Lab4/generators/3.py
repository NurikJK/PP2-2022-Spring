def krat(n):
    for i in range(n):
        if i % 3 == 0 and i % 4 == 0:
            yield i
n = int(input())
for i in krat(n):
    if i == n - 1:
        print(i,end = ".")
    else:
        print(i,end = ", " )
