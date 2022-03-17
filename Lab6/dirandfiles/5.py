import os
cnt = 0
file = input()
inp = ''
if os.path.exists(file):
    file = open(file, mode = 'a')
    while inp != 'save':
        inp = input()
        if inp != 'save': file.write(inp + '\n')
    file.close()
else: print('File does not exist')