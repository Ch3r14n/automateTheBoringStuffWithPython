#! python3

import re

password = input('Your input here: ')

eightChar = re.compile(r'.{8,}')
lowerCase = re.compile(r'[a-z]')
upperCase = re.compile(r'[A-Z]')
numbers = re.compile(r'[0-9]')

if eightChar.search(password) is None or \
        lowerCase.search(password) is None or \
        upperCase.search(password) is None or \
        numbers.search(password) is None:
    print('This is not a strong password')
else:
    print('This is a strong password')
