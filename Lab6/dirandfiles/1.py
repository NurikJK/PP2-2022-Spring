import os

path = input("Enter path: ")
if os.path.isdir(path):
    if not os.listdir(path): 
        print("There are no folders and files")
        exit()

    print("Folders and files: ")
    for i in os.listdir(path):
        print(i)

    print("\nFolders:")
    for i in os.listdir(path):
        if os.path.isdir(path + '\\' + i):print(i)

    print("\nFiles: ")
    for i in os.listdir(path):

        if os.path.isfile(path + "\\"+ i):print(i)
else: print('No match')