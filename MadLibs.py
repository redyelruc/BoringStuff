'''Create a Mad Libs program that reads in text files and lets the user add their own text anywhere the word
ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file. For example, a text file may look like this:
The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was
unaffected by these events.
The program would find these occurrences and prompt the user to replace them.
Enter an adjective:
silly
The following text file would then be created:
The results should be printed to the screen and saved to a new text file.'''

import re
import pyinputplus as pyip

# opens the file

def replace_for_keyword(list_of_words):
    list_of_keywords = ['NOUN', 'ADJECTIVE', 'VERB']
    for keyword in list_of_keywords:
        for current_word in list_of_words:
            if keyword in current_word:
                current_index = list_of_words.index(current_word)
                new_word = pyip.inputStr('Please enter a %s:' % keyword.lower())
                list_of_words.remove(current_word)
                list_of_words.insert(current_index, new_word)
    return list_of_words

open_file = open('C:\\Users\\redye\\Documents\\madlibs.txt')
current_version = open_file.read()
current_list = current_version.split()
final_list = replace_for_keyword(current_list)
final_version = ' '
final_version = final_version.join(final_list)

open_file.close()
open_file = open('C:\\Users\\redye\\Documents\\madlibs.txt', 'w')
open_file.write(final_version)
open_file.close()



# loop through words looking for ADJ, NOUN etc.

# Ask user to replace them

# print the finished text

# save the file