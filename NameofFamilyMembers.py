import random
import pyinputplus as pyip
import shelve

def reveal():  #prints the members of the family
    for index, member in enumerate(family_members):
        print("person " + str(index + 1) + " is " + member)

family_members = {}
while True:
    print("Enter the name of family member " + str(len(family_members) + 1))
    print("Or press enter to stop.")
    name = input()
    if name == "":
        break
    elif name.isalpha() == False:
        print('That\'s not a name. Are you dyslexic? Try again.')
        continue
    elif name in family_members:
        print("you've already entered that name.")
        continue
    elif name.istitle() == False:
        name = name.lower()
        first_letter = name[0]
        rest_of_name = name[1 : len(name)]
        first_letter = first_letter.upper()
        name = first_letter + rest_of_name
        family_members += [name]
print('In order of importance, you think that ')
reveal()
random.shuffle(family_members)
if 'Rampage' in family_members:
    family_members.remove('Rampage')
family_members.insert(0, 'Rampage')
print('but actually, the order should be ')
reveal()



