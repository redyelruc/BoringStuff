import pyinputplus as pyip

types_of_food = {'bread': ['wheat', 'white', 'sourdough'], 'protein type':
    ['chicken', 'turkey', 'ham', 'tofu']}
print('Welcome to Fatso\'s Sanwiches')
while True:
    choice_made =[]
    for food, choices in types_of_food.items():
        print('What type of %s would you like?'% food )
        choice_made.append(pyip.inputMenu(types_of_food[food], lettered=True))
    if pyip.inputYesNo('Would you like cheese?') == 'yes':
        print('What type of cheese would you like?')
        choice_made.append(pyip.inputMenu(['mozzarella', 'cheddar', 'parmesan'], lettered = True))
    else:
        choice_made.append('')
    if pyip.inputYesNo('Would you like any sauce?') == 'yes':
        print('What type of sauce would you like?')
        choice_made.append(pyip.inputMenu(['ketchup', 'brown sauce', 'mayo', 'salad cream'], lettered = True))
    else:
        choice_made.append('')
    print('So that\'s a sandwich on %s bread with %s,  %s, %s.'
          %(choice_made[0], choice_made[1], choice_made[2], choice_made[3]))
    if pyip.inputYesNo('Would you like another sandwich?') == 'no':
        break