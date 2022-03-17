def letters(s):
    uppercase = sum(1 for i in s if i.isupper())
    lowercase =  sum(1 for i in s if i.islower())
    print('Uppercase: ' + str(uppercase), '\nLowercase: ' + str(lowercase))
letters(input())