arr = list(map(int, input().split()))
current = 0
ok = False
l = len(arr) - 1
for i in range(len(arr)):
    if i > current:
        ok = False
        break
    if arr[i] + i > current:
        current = arr[i]+i
    if current >= l:
        print(1)
        ok = True
        break
if ok == False:
    print(0)