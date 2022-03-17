def multiplesum(arr):
    ms = 1
    for i in arr: ms *= i
    print(ms)
multiplesum(list(map(int,input().split())))
