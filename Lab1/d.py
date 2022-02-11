def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"

n = int(input())
string = input()
if string == "k":
    cnt = int(input())
    res = n / 1024
    # print('%.3f' % res) 
    print(toFixed(res, cnt))
elif string == "b":
    print(n * 1024)