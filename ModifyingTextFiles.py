# don't ned the whole pathlib and don't want to
from pathlib import Path
import pyinputplus as pyip
import os


'''name_of_file = 'C:\\Users\\redye\\Documents\\sampletextfile.txt'

# creates a path object
sample_path = Path(name_of_file)

# creates a file object
openfile = open(name_of_file)

print(openfile.read())
'''
# opens a file that is writeable
newopenfile = open(Path('C:\\Users\\redye\\Documents\\sonnet29.txt'), 'w')

# gets the text to write to th file
new_text_for_file = pyip.inputStr('Sonnet 29 is ready to be written. Please input your text:')

#writes the text and closes the file
newopenfile.write(new_text_for_file + '\n')
newopenfile.close()
print('File has been saved.')

# reopen the file, print the new contents and close it again
newopenfile = open(Path('C:\\Users\\redye\\Documents\\sonnet29.txt'))
print(newopenfile.read())
newopenfile.close()


#open file that is appendable
newopenfile = open(Path('C:\\Users\\redye\\Documents\\sonnet29.txt'), 'a')
# gets the text to add to th file
new_text_for_file = pyip.inputStr('Sonnet 29 is ready to be extended. Please input your text:')

#appendss the text and closes the file
newopenfile.write(new_text_for_file)
newopenfile.close()
print('File has been saved.')

# reopen the file, print the new contents and close it again
newopenfile = open(Path('C:\\Users\\redye\\Documents\\sonnet29.txt'))
print(newopenfile.read())
newopenfile.close()