import re
text = '''Hi World! fmdW3 fpidj
My name is Python
ASDfffffff Dfdffdf'''
f = re.findall(r'[A-Z][a-z]+',text)
print(f)    