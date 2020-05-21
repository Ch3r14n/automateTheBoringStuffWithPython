#! python3

import pyinputplus as pyip

price = 0

breadType = {'wheat': 5,
             'sourdough': 10,
             'white': 15}

response = pyip.inputMenu(list(breadType.keys()))

price += breadType[response]

proteinType = {'tofu': 30,
               'ham': 40,
               'chicken': 50,
               'turkey': 60}

response = pyip.inputMenu(list(proteinType.keys()))

price += proteinType[response]

prompt = 'Would you like cheese in your sandwich?\n'
response = pyip.inputYesNo(prompt)
if response == 'yes':

    cheeseType = {'cheddar': 10,
                  'mozzarella': 15,
                  'Swiss': 20}

    response = pyip.inputMenu(list(cheeseType.keys()))

    price += cheeseType[response]

else:
    pass

extras = 5

prompt = 'Would you like mayo in your sandwich?\n'
response = pyip.inputYesNo(prompt)

if response == 'yes':
    price += extras

prompt = 'Would you like mustard in your sandwich?\n'
response = pyip.inputYesNo(prompt)

if response == 'yes':
    price += extras

prompt = 'Would you like lettuce in your sandwich?\n'
response = pyip.inputYesNo(prompt)

if response == 'yes':
    price += extras

prompt = 'Would you like tomato in your sandwich?\n'
response = pyip.inputYesNo(prompt)

if response == 'yes':
    price += extras

true = True

while true:
    prompt = 'How many sandwiches would you like?\n'
    response = pyip.inputInt(prompt)
    if response > 0:
        true = False

price *= response

print('Rs.%s' % price)
