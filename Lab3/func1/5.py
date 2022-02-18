import itertools

def perms(s): 
    print('\n'.join([str(i) for i in itertools.permutations(s)]))

print(perms(input()))
