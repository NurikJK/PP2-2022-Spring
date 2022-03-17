import os

path = input()

if os.path.exists(path):
    for i in os.listdir(path):
        if os.path.isdir(i):
            pathforfolder = path + '\\' + i
            print(str(i) + ':')
            for i in os.listdir(pathforfolder):print(i,end = ' ')
        else:print(i)
else: print('Pass does not exist!')