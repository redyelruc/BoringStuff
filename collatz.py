def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return number * 3 + 1


print("please type a number")
try:
    number_entered = int(input())
    while collatz(number_entered) > 1:
        print(collatz(number_entered))
        number_entered = collatz(number_entered)
    print(collatz(number_entered))
except ValueError:
    print("Sorry, you must enter a number")
