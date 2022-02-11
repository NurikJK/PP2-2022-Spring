i = 0
index = 0
for i in range(int(input    )):
    s = input()
    for i in range(len(s)):
        if s[i] == "@":
            index = i
    if s[index:len(s)] == "@gmail.com":
        print(s[0:index])