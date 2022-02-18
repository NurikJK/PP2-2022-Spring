def fahr(f):
    c = ((f - 32) * (5/9))
    return round(c)
    # return ((f - 32) * (5/9))
f = int(input())
print(fahr(f))