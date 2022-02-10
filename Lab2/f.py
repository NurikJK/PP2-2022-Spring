n = int(input())
doc = {}
max = -999
for i in range(n):
    name,money = input().split()
    money = int(money) 
    if name in doc:
        doc[name] += money
    else:
        doc[name] = money

for key, value in doc.items():
    if value > max:
        max = value
for key, value in sorted(doc.items()):
    if max - value == 0:
        print(key + " is lucky!")
    else:
        print(key + " has to receive " + str(max - doc[key]) + " tenge ")