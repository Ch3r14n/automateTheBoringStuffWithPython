#! python3

import random
import time

numberOfQuestions = 10
correctAnswers = 0
for questionNumber in range(numberOfQuestions):
    # Pick two random numbers:
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)

    answer = '#%s: %s x %s = ' % (questionNumber, num1, num2)

    print(answer)

    input(answer, allowRegexes=['^%s$' % (num1 * num2)], blockRegexes=[('.*', 'Incorrect!')], timeout=8, limit=3)

    numberOfTries = int(input)

    if answer.time > 8:
        print('Out of time!')
    if numberOfTries > 3:
        print('Out of tries!')
    else:
        print('Correct!')
        correctAnswers += 1

    time.sleep(1)  # Brief pause to let user see the result.
print('Score: %s / %s' % (correctAnswers, numberOfQuestions))
