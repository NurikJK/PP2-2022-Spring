import os
cnt = 0

with open(input(), 'r') as file:
    for line in file:cnt += 1

print("Number of lines in file: " + str(cnt))
