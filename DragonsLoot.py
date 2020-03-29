"""Write a function named addToInventory(inventory, addedItems),
where the inventory parameter is a dictionary representing the
player’s inventory (like in the previous project) and
the addedItems parameter is a list like dragonLoot.
The addToInventory() function should return a dictionary
that represents the updated inventory. Note that the addedItems list
can contain multiples of the same item."""

def addtoinventory(inventory, added_items):
    for i in added_items:
        if i in inventory:
            inventory[i] += 1
        else:
            inventory[i] = 1
    return inventory

def print_inventory(inventory, leftWidth, rightWidth):
    print('INVENTORY'.center(leftWidth + rightWidth, '-'))
    for k, v in inventory.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))

franks_inventory = {'coin' : 1, 'potion' : 3, 'diamond' : 11}
dragons_loot = ['coin', 'potion', 'coin', 'coin', 'diamond', 'ruby']
wizards_loot = ['potion', 'potion', 'magic dust']
print(franks_inventory)
print_inventory(addtoinventory(franks_inventory, dragons_loot + wizards_loot), 15, 3)


