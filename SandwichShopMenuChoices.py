import pyinputplus as pyip

types_of_food = {'bread': ['wheat', 'white', 'sourdough'], 'filling':
    ['chicken', 'turkey', 'ham', 'tofu']}

prices = {'wheat' : 1.5, 'white': 1.6, 'sourdough': 2, 'chicken': 1, 'turkey':1.2, 'ham': 1.5,
          'tofu': 2, 'mozzarella': 0.5, 'cheddar': 0.4,'parmesan': 0.5, 'ketchup': 0.2,'brown sauce':0.2,
          'mayo': 0.2, 'salad cream': 0.1}

# function to add choie made to list and to fetch its price
def process_choice(chosen):
    choice_made.append(chosen)
    return prices[chosen]

print('Welcome to Fatso\'s Sandwiches')

while True:
    choice_made =[]
    sandwich_price = 0
    for food, choices in types_of_food.items():
        print('What type of %s would you like?'% food )
        item_chosen = pyip.inputMenu(choices, lettered=True)
        sandwich_price = sandwich_price + process_choice(item_chosen)
    # check if wants cheese and find out which one
    if pyip.inputYesNo('Would you like cheese?') == 'yes':
        print('What type of cheese would you like?')
        item_chosen = pyip.inputMenu(['mozzarella', 'cheddar', 'parmesan'], lettered = True)
        sandwich_price = sandwich_price + process_choice(item_chosen)
    else:
        choice_made.append('')
    # check if wants sauce and find out which one
    if pyip.inputYesNo('Would you like any sauce?') == 'yes':
        print('What type of sauce would you like?')
        item_chosen = pyip.inputMenu(['ketchup', 'brown sauce', 'mayo', 'salad cream'], lettered = True)
        sandwich_price = sandwich_price + process_choice(item_chosen)
    else:
        choice_made.append('')
    # shows order so far
    print('So that\'s a sandwich on %s bread with %s,  %s, %s.'
          %(choice_made[0], choice_made[1], choice_made[2], choice_made[3]))
    print('Your sandwich costs £%s'% sandwich_price)
    if pyip.inputYesNo('Would you like another sandwich?') == 'no':
        break