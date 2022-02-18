def prime(x):
    i = 2
    if x < 2:
        return False 
    while i != x:
        if x % i == 0:
            return False
            break
        i += 1
    return True
x = int(input())
print(prime(x))