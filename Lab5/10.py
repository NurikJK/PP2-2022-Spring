import re

text = 'CamelCaseLol'
# output = camel_case_lol
f = re.sub(r'(?!^)(?=[A-Z][a-z]+)', '_', text).lower()
# f = re.sub(r'(?!^)(?=[A-Z][a-z]+[^A-Z]*)', '_', text).lower()

print(f)
