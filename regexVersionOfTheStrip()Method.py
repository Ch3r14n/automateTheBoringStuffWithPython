#! python3

import re

data = input('Your input here: ')


def regStrip(item, char=' '):
    if char == ' ':
        regex = re.compile(r'^(\s*)(.*?)(\s*)$')
        return regex.sub(r'\2', item)
    else:
        regex = re.compile('%s' % char)
        return regex.sub(' ', item)


print('''Raw String:%s
Stripped String:%s''' % (data, regStrip(data)))
