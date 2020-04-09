'''asks the user for some text;
checks whether the entered text is a palindrome, and prints result.
assume that an empty string isn't a palindrome;
treat upper- and lower-case letters as equal;
spaces are not taken into account during the check - treat them as non-existent;
there are more than a few correct solutions - try to find more than one.'''

#function to check if input is a pallindroem
def pallindrome(text):
    for i in range(len(text)):
        if text[i] == text[-(i+1)]:
            continue
        else:
            return 'Not a pallindrome'
    return 'Pallindrome'

# function to strip any character not in the alphabet
def strip_non_alpha(text):
    spaceless_text = ''
    text = text.lower()
    for i in range(len(text)):
        if ord(text[i]) < 97 or ord(text[i]) > 122:
            continue
        spaceless_text += text[i]
    return spaceless_text

string = input('type here: ')
newstring = strip_non_alpha(string)
print(pallindrome(newstring))