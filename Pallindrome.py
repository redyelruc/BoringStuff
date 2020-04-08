'''asks the user for some text;
checks whether the entered text is a palindrome, and prints result.
assume that an empty string isn't a palindrome;
treat upper- and lower-case letters as equal;
spaces are not taken into account during the check - treat them as non-existent;
there are more than a few correct solutions - try to find more than one.


def pallindrome(text):
    list_of_chars = list(text)
    for i in range(len(list_of_chars)):
        if list_of_chars[i] == list_of_chars[-(i+1)]:
            continue
        else:
            return False
    return True

def stripnonalpha(text):
    spaceless_text =''
    text = text.lower()
    for i in range(len(text)):
        if ord(text[i]) < 97 or ord(text[i]) > 122:
            continue
        spaceless_text += text[i]
    return spaceless_text

string = input('type here:')
newstring = stripnonalpha(string)
print(pallindrome(newstring))'''

text = input('Give your text:')
text = text.replace(' ', '').upper()
reverse = ''

for i in text:
    reverse = i + reverse
if text == reverse and len(text) != 0:
    print('Palindrome!')
else:
    print('No palindrome')