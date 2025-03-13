import re

stripRegex = re.compile(r'\s')

mo = stripRegex.sub('', input('Please enter string: '))
print(mo)