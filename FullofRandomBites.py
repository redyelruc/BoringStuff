import random

spam = [["Cuisle", "Thalita", "Rampage"], ["love", "bites", "bollix"]]
for i in range(5):
    print(random.choice(spam[0]) + ' is full of '+ random.choice(spam[1]))

