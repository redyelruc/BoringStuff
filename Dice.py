'''Make a class Die with one attribute called sides, which has a default
value of 6. Write a method called roll_die() that prints a random number
between 1 and the number of sides the die has. Make a 6-sided die and roll it
10 times. Make a 10-sided die and a 20-sided die. Roll each die 10 times.'''

import random

class Die:
    # creates a dice with a number of sides, default is 6
    def __init__(self, sides = 6):
        self.sides = sides

    # roll a dice a number of times
    def roll_die(self, times):
        for i in range(times):
            print('Roll ' + str(i+1) + ':  You rolled a ' + str(random.randint(1,self.sides)))

six_sided_dice = Die(6)
six_sided_dice.roll_die(5)

ten_sided_dice = Die(10)
ten_sided_dice.roll_die(5)

