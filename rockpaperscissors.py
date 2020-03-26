import random, sys

tie = 0
win = 0
loss = 0

while True:
    while True:
        print(
            "Wins - "
            + str(win)
            + "    Losses - "
            + str(loss)
            + "    Ties - "
            + str(tie)
        )
        print("ROCK, PAPER, SCISSORS")
        print("Enter your move: (r)ock, (p)aper, (s)cissors, (q)uit")

        answer = input()
        if answer == "r":
            print("ROCK versus...")
            answer = 1
            break
        elif answer == "p":
            print("PAPER versus...")
            answer = 2
            break
        elif answer == "s":
            print("SCISSORS versus...")
            answer = 3
            break
        elif answer == "q":
            answer = 4
            print("Thanks for playing.")
            sys.exit()
    else:
        continue
    computer = random.randint(1, 3)  # gets computer to choose
    if computer == 1:
        print("ROCK")
    elif computer == 2:
        print("PAPER")
    else:
        print("SCISSORS")
    if answer == computer:
        print("It's a tie")
        tie = tie + 1
    elif computer - answer == 1 or computer - answer == -2:
        print("You lose!")
        loss = loss + 1
    else:
        print("You win!")
        win = win + 1
