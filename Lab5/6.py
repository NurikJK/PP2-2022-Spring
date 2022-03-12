import re

text = 'Hello, world. Hello: python.'
# output = Hello::world::Hello::python:
f = re.sub('[,. ]', ':', text)
print(f)