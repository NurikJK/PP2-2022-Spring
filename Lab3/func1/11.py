sign = ":;!,.? ’"
def palindrome(s):
    s = s.lower()
    print(s)
    if s == s[::-1]:
        return True
    return False
s = input()
for i in sign:
    s = s.replace(i, '')
print(palindrome(s))