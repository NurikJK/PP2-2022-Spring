import re
text = '''Words: abdsmo sbahbd aprkeb asomb a000b'''
f = re.findall(r'\w*a[0b]\w*', text)

print(f)