import os,shutil

alphabet = 'ABCDEGHIJKLMNOPQRSTUVWXYZ'

folder = input('Enter foldername: ')
if not os.path.exists(folder):
    os.mkdir(folder)

dst = os.getcwd() + '\\' + folder
for i in range(len(alphabet)):
    if not os.path.exists(alphabet[i]):
        file = open(alphabet[i],'w')
        file.close()
        file = open(alphabet[i],mode = 'a')
        file.write(alphabet[i])
        file.close()
        src = os.getcwd() + '\\' + str(alphabet[i])
        shutil.move(src, dst)
# Second another solution
# for i in range(25):
#     if not os.path.exists(str(chr(i+65))):
#         file = open(strchr(i+65),'w')
#         file.close()
#         file = open(str(chr(i+65)))
#         file.write(str(chr(i+65))
#         file.close()
#         src = os.getcwd() + '\\' + str(chr(i+65))
#         shutil.move(src, dst)
