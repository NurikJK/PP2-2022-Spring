n = int(input())
arr = list(map(int, input().split()))[:n]
sum = 1
arr = sorted(arr)
a = arr[n-1]
b = arr[n-2]

print(a*b)