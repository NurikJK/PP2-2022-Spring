def legs(numheads,numlegs):
    return round((4 * numheads - numlegs)/2) , round(numheads - ((4 * numheads - numlegs) / 2))
numheads,numlegs = map(int, input().split())
print(legs(numheads, numlegs))
# print(legs(int(input()).int(input())))
# 4x + 2y = numlegs 
#  x + y = numheads
# x = numheads - y 
# 4 (numheads - y) + 2y = numlegs
# 4 * numheads - 2y = numlegs
# -2y = numlegs - 4numheads
# y = (4 * numheads - numlegs)/2    