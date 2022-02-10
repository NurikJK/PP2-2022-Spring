n = int(input())

col = []
current = 0

for i in range(n):
    arr = list(map(str, input().split()))
    if arr[0] == "1":
        col.append(arr[1])
    else:
        current += 1

# for i in range(current):
#     print(col[i], end = " ")
print(*[col[i] for i in range(current)])