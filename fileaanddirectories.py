from pathlib import Path
import os

print(Path.cwd())
#change directory
os.chdir(('C:\\Windows\\System32'))
# get the current working directory
print(Path.cwd())
# get the default home directory
print(Path.home())


filepathname = 'C:\\Users\\redye\\Documents\\Santiago.docx'

# testing tools that manipulate the string of a filepath

# splits filepath name into directory and file and stores in tuple
print(os.path.split(filepathname))

# get the name of the file seperated from the complete file path
print(os.path.basename(filepathname))

# get the sixe of a file
print(os.path.getsize(filepathname))

# seperate the file path into a list of strings of each part
print(filepathname.split(os.sep))

name_of_directory = (os.path.dirname(filepathname))

#list the contents of a directory
print(os.listdir(name_of_directory))

# using a loop to get the total size of all the files in a certain directory
total_size = 0
for file_name in os.listdir(name_of_directory):
    total_size = total_size + os.path.getsize(os.path.join(name_of_directory, file_name))
print(total_size)

# changing the string into a path object
name_of_path = Path(name_of_directory)

# get a list of every individual path in a named directory
print(list(name_of_path.glob('*')))

# get a list of every docx file in a named directory
print(list(name_of_path.glob('*.docx')))
for textFilePathObj in name_of_path.glob('*.docx'):
    print(textFilePathObj) # Prints the Path object as a string.
    # Do something with the doc file.

# these methods only work on Path objects
# checking to see if a path exists
print(name_of_path.exists())

# checking if the path exists and is a file
print(textFilePathObj.is_file()) # returns True
print(name_of_path.is_file()) # returns False

# checking if the path exists and is a directory
print(textFilePathObj.is_dir())  #returns False
print(name_of_path.is_dir())   # returns True