# module to validate input
import pyinputplus as pyip

# Dictionary containing value for each row ascending through the digits (0-2)
# ( with spaces after digits so they are not all clumped together

led = {'row1' : ['###  ', '#  ', '###  '],
       'row2' : ['# #  ', '#  ', '  #  '],
       'row3' : ['# #  ', '#  ', '###  '],
       'row4' : ['# #  ', '#  ', '#    '],
       'row5' : ['###  ', '#  ', '###  ']}

# Ask for input and force user to enter a positive integer
while True:
    num_entered = pyip.inputInt('please enter a number to digitalize?: ')
    if num_entered <0:
        print('The number cannot be negative. Try again.')
        continue
    break

# Convert number entered to a list containing individual digits
list_of_digits = list(str(num_entered))

# Loop through rows
for row_number in range(5):
    # Loop to print each digit
    for i in list_of_digits:
        print(led['row' + str(row_number + 1)][int(i)], end = '')
    # Get a new line
    print()
