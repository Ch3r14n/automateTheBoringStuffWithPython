#! python3

import re

dateRegex = re.compile(r'''(
    ([0][1-9]|[1][0-9]|[2][0-9]|[3][0-1])
    (\s|/|\.)
    ([0][1-9]|[1][1-2])
    (\s|/|\.)
    ([1][0-9][0-9][0-9]|[2][0][0-9][0-9])
    )''', re.VERBOSE)

text = str(input('Your input here: '))

matches = []
for groups in dateRegex.findall(text):
    date = '/'.join([groups[1], groups[3], groups[5]])
    matches.append(date)

if len(matches) > 0:
    print('Dates found:')
    print('\n'.join(matches))
else:
    print('No dates found.')
