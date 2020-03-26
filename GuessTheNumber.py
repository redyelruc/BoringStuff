#  this is a guess the number game
import random

secret_number = random.randint(1, 20)
print("I am thinking of a number between 1 and 20. Can you guess what it is?")
for i in range(1, 6):
    guessed = input()
    if int(guessed) < secret_number:
        print("too low, guess again.")
    elif int(guessed) > secret_number:
        print("too high, guess again.")
    else:
        break
if int(guessed) == secret_number:
    print("well done, you took " + str(i) + " guesses")
else:
    print('Bad luck. I was thinking of ' + str(secret_number))
