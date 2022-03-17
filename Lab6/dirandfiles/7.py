import os

frompath = input('Enter path to copy: ')

topath = input('Enter path to paste: ')

with open(topath, 'w') as copy_txt:
    with open(frompath) as paste_txt:
        copy_txt.write(str(paste_txt.read()))
    with open(topath) as copy_txt:
        print(copy_txt.read())