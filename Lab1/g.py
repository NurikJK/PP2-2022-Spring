a = input()
number = 0

for i in range(len(a)):
    number += int(a[i]) * (2**(len(a) - i - 1))

print(number)