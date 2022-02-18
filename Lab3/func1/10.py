def unique(arr):
    col = []
    for i in arr:
        if i not in col:
            col.append(i)
    return col
arr = list(map(int, input().split()))
print(unique(arr))