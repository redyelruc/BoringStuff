# Random Coin Flip

import random


final_total = 0
# set up experiemnt to run 10000 times
for x in range(10000):
    #  create list of random coin flips
    list_of_flips = []
    for y in range(100):
        this_flip = random.randint(0, 1)
        if this_flip == 0:
            list_of_flips.append('heads')
        else:
            list_of_flips.append('tails')

    #  check for 6 in a row
    y = 0
    streak = 0
    total_streak = 0
    while y < 99:
        current_toss = list_of_flips[y]
        next_toss = list_of_flips[y+1]
        if current_toss == next_toss:
            streak += 1
            if streak == 5:
                total_streak += 1
                streak -= 1
        else:
            streak = 0
        y += 1
    print(total_streak)
    final_total = final_total + total_streak
print('Chance of streak: %s%%' % (final_total / 94 / 10000))

