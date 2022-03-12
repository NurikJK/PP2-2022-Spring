import re

text = 'СamelCaseLol'
f = re.sub(r'(?!^)(?=[A-Z][a-z]+)', ' ', text)
print(f)