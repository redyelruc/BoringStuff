import pprint

player_list = {'Aidan' : {'arrows' : 1, 'bullets' : 23, 'bows' : 1, 'guns' : 4}, 'Thalita' : {'arrows' : 12, 'bullets' : 3, 'bows' : 2, 'guns' : 1}}


def display_inventory(players):
    grand_total = 0
    for name, inventory in players.items():
        total_items = 0
        print('In ' + name + '\'s inventory, there are:')
        for item in inventory.items():
            print(str(item[1]) + ' ' + str(item[0]))
            total_items += item[1]
        print('Total items = ' + str(total_items))
        grand_total += total_items
    print('The grand total of items in the game is ' + str(grand_total))

def check_inventory(players, weapon):
    num_of_weapons = 0
    for name, inventory in players.items():
        num_of_weapons += inventory.get(weapon, 0)
    print('Total ' + str(weapon) + ': ' + str(num_of_weapons))



display_inventory(player_list)
check_inventory(player_list, 'arrows')