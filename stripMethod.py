# takes a string and mimics the strip() method
# if no other arguments are passed other than the string to strip
# then whitespace characters are removed from beginning and end of string
# otherwise the characters specified in the second argument to the function will be removed from the string

import re

# stripRegex = re.compile(r'\s')

# mo = stripRegex.sub('', input('Please enter string: '))
# print(mo)

def stripMimic(str, char=' '):
    stripRegex = re.compile(f'{char}')
    strippedStr = stripRegex.sub('',str)
    return strippedStr

print(stripMimic(input('Please enter string: '),'f'))