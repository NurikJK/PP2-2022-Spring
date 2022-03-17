import os

file = input('Enter file/folder name: ')

if os.path.isfile(file):
    print("File exists")
    print("Press 1 to write text\nPress 2 to rewrite the file\nPress 3 to change")
    func = int(input())
    if func == 1:
        file = open(file, 'a')
        file.write(input('Add new txt: ') + '\n')
        file.close()
    elif func == 2:
        file = open(file, 'w')
        file.write(input('New txt: '))
        file.close()
    elif func == 3:
        os.chdir(input('Enter path: '))
    else: print('Incorrect option')
else: print("Does not exist")
