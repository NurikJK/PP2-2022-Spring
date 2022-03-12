import re
text = 'sdjabeabdul apmsma andsnb baby'

f = re.findall(r'\w*[.+a.+b]\w*',text)

print(f)