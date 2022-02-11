string = input()
sum = 0

for i in range(len(string)):
    sum = sum + int(ord(string[i]))

if sum < 300:
    print("Oh, no!")
else:
    print("It is tasty!")