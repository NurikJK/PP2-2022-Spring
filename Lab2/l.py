s = input()

first = ['(', '[', '{']
second = [')', ']', '}']

arr = []
ok = True
for i in s:
    if i in first:
        arr.append(i)
    else:
        index = second.index(i)
        if len(arr) != 0 and first[index] == arr[len(arr) - 1]:
            arr.pop()
        else:
            ok = False
            break

print("Yes") if ok == True and len(arr) < 1 else print("No")

#[]
#
#
#