import re
text = 'sdjabeabdul apmsma andsnb dsi_dsm dskdk_ds'
f = re.findall(r'[a-z]+_[a-z]+',text)
print(f)