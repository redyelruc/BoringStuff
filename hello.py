print("Hello world")
print("What is your name?")  # ask for the useer's name
my_name = input()
print("Nice to meet you, " + my_name)
print("Your name is ", len(my_name), "characters long")
print("How old are you?")
my_age = input()
my_age = int(my_age)
if my_age <= 25:
    print("Lucky you!")
    print("Next year, you'll only be ", my_age + 1, "years old.")
elif my_age > 40:
    print(
        "Fuck me! Next year, you'll be", my_age + 1, " - if you make it that far."
    )
else:
    print("Looking good. Next year, you'll be", my_age + 1, "years old")
