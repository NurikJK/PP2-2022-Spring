n = int(input())

if n % 2 == 1:
    for i in range(n):
        for j in range(n):
            if i + j < n - 1: 
                print(".",end = "")
            else:
                print("#",end = "")
        print()
cur = 0    
if n % 2 == 0:
    for i in range(n):
        for j in range(n):
            if j - cur <= i and i >= j:
                print("#",end = "")
            else:
                print(".",end = "")
        print()
        cur += 1
#   
#   #...   
#   ##..
#   ###.
#   ####
#   0,0 1,0 2,0 3,0
#   0,1 1,1 1,2 1,3
#   0,2 1,2 2,2 2,3 
#   0,3 1,3 3,2 3,3 