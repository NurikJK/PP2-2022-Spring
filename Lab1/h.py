string = input()
m = input()
cnt = 0
for i in range(len(string)):
    if string[i] == m:
        cnt += 1
if cnt == 1:
    for i in range(len(string)):
        if string[i] == m:
            print(i,end = " ")
            break  
if cnt > 1:
    for i in range(len(string)):
        if string[i] == m:
            print(i, end= " ")
            break
    rev = string[::-1]
    for i in range(len(rev)):
        if rev[i] == m:
            print(len(rev) - i - 1,end = " ")
            break