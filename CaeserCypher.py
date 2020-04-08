
import pyinputplus as pyip

'''asks the user for one line of text to encrypt;
asks the user for a shift value (an integer number from the range 1..25 
- note: you should force the user to enter a valid shift value (don't give up and don't let bad data fool you!)
prints out the encoded text.'''

# Get the message and the code shift and validate them before progressing
text = pyip.inputStr('Please enter your message: ')
while True:
    shiftby = pyip.inputInt('Please enter a number to encode by: ')
    if shiftby < 0 or  shiftby > 25:
        print('Sorry, it must be between 0 and 25.')
        continue
    break

cypher = ''
# go through text one character at a time
for character in text:
    # if not an alphabetic character, disregard it.
    if not character.isalpha():
        cypher += character
        continue
    # Treat upper and lower cases as seperate codes
    if character.isupper():
        character = ord(character)
        character += shiftby
        # if gone past 'Z', back to start
        if character > 90:
            character -= 25
    elif character.islower():
        character = ord(character)
        character += shiftby
        # if gone past 'z', back to start
        if character > 122:
            character -= 25
    # add character to the cypher
    cypher += (chr(character))
print(cypher)

# check if user wants to decypher message
print()
decypher = pyip.inputYesNo('Do yo want to decypher the message now?')

if decypher:
    # to decypher the code
    text = ''
    for character in cypher:
        if not character.isalpha():
            text += character
            continue
        if character.isupper():
            character = ord(character)
            character -= shiftby
            # if gone past 'Z', count back from 'z'
            if character < 65:
                character += 25
        elif character.islower():
            character = ord(character)
            character -= shiftby
            # if gone past 'a', count back from 'z'
            if character <97:
                character += 25
        # add character to the cypher
        text += (chr(character))

    print(text)

