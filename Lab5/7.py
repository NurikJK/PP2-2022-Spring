import re

text = 'Hello_world'
#output = HelloWorld
f = ''.join(x.capitalize() or '_' for x in text.split('_'))
print(f)
