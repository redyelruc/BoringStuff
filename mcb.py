# mcb.pyw - Saves and loads pieces of text to the clipboard
# Usage: py.exe mcb.pyw save <keyword> saves clipboard to keyword
#        py.exe mcb.pyw <keyword> loads keyword to clipboard
#        py.exe mcb.pyw list loads all keywords to the clipboard

import shelve
import pyperclip
import sys

mcb_shelf = shelve.open('mcb')

# Save clipboard content.
# if the first command line argument is save, the second one is the keyword
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    # paste the clipboard to the keyword
    mcb_shelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    # List keywords and load content.
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcb_shelf.keys())))
    elif sys.argv[1] in mcb_shelf:
        pyperclip.copy(mcb_shelf[sys.argv[1]])

mcb_shelf.close()