import pyinputplus as pyip
import random
import time

# Manually doing the multiplication quiz without time limits or attempt limit
'''number_of_questions = pyip.inputInt('How many questions do you want in the quiz?', lessThan=11)
correct_answers = 0
for question_number in range(int(number_of_questions)):
    number1 = random.randint(1,9)
    number2 = random.randint(1,9)
    prompt = '#%s: %s x %s = ' % (question_number + 1, number1, number2)
    answer = pyip.inputInt(prompt)
    if answer == number1 * number2:
        print('correct')
        correct_answers +=1
print('You got ' + str(correct_answers) + ' correct answers.')
percentage_correct = correct_answers/number_of_questions * 100
print('That\'s ' + str(percentage_correct) + '%')
if percentage_correct > 65:
    print('Well done!')
else:
    print('Must try harder!')'''

# same code using regexes to check the answers, plus time limits and attempt
number_of_questions = pyip.inputInt('How many questions do you want in the quiz?', lessThan=11)
correct_answers = 0
for question_number in range(int(number_of_questions)):
    try:
        # Right answers are handled by allowRegexes.
        # Wrong answers are handled by blockRegexes, with a custom message.
        number1 = random.randint(1, 9)
        number2 = random.randint(1, 9)
        prompt = '#%s: %s x %s = ' % (question_number + 1, number1, number2)
        pyip.inputStr(prompt, allowRegexes=['^%s$' % (number1 * number2)], blockRegexes=[('.*', 'Incorrect!')],
                  timeout=8, limit=3)
    except pyip.TimeoutException:
        print('Out of time!')
    except pyip.RetryLimitException:
        print('Out of tries!')
    else:
        # This block runs if no exceptions were raised in the try block.
        print('Correct!')
        correct_answers += 1
        time.sleep(1) # Brief pause to let user see the result.
print('Score: %s / %s' % (correct_answers, number_of_questions))