my_bird = {'size' : 'tiny', 'colour' : 'blue', 'disposition' : 'bollix'}

while True:
    print('what do you want to know about your pet? (blank to quit)')
    trait = input()
    if trait == '':
        break

    #  now check if trait is already stored
    if trait in my_bird:
        print('Your bird\'s ' + trait + ' is ' + my_bird[trait])
    else:
        print('I have no information for this trait.')
        print('What is its ' + trait)
        trait_answer = input()
        my_bird[trait] = trait_answer
