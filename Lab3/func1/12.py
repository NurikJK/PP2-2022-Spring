def histogram(arr):
    for i in arr:
        for j in range(i):
            print("*",end="")
        print()

histogram(list(map(int, input().split())))