n = int(input())
demons = {}
hunters = {}

for i in range(n):
    name, spec = input().split()
    if spec in demons:
        demons[spec] += 1
    else:
        demons[spec] = 1

m = int(input())

for i in range(m):
    name, spec, num = input().split()
    if spec in hunters:
        hunters[spec] += int(num)
    else:
        hunters[spec] = int(num)

alive = 0
for spec in demons:
    if not spec in hunters:
        alive += demons[spec]
    elif demons[spec] - hunters[spec] >= 0 and spec in hunters:
        alive += demons[spec] - hunters[spec]

print('Demons left: ' + str(alive))