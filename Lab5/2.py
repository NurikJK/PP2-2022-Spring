import re
text = '''Words: abbbmfdm babby abbmfd aifmdbb abdms ab abbb abbbbbbbbbbbbbbbbbbbb'''

f = re.findall(r'\w*a[b]{2,3}\w*', text)

print(f)