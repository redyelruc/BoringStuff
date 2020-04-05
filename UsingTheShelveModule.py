import shelve

'''# create a shelf file called 'mydata'
shelf_File = shelve.open('mydata')
cats = ['Zophie', 'Pooka', 'Simon']

# saves the list above 'Cats' in the under the cats key in the shelffile and closes file
shelf_File['cats'] = cats
shelf_File.close()'''

# reopens the shelffile
shelf_File = shelve.open('mydata')
#checks what keys there are
print(list(shelf_File.keys()))
# checks what values there are
print(list(shelf_File.values()))
shelf_File.close()