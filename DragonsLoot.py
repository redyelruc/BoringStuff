# Write a function named addToInventory(inventory, addedItems),
# where the inventory parameter is a dictionary representing the
#  player’s inventory (like in the previous project) and
#  the addedItems parameter is a list like dragonLoot.
#  The addToInventory() function should return a dictionary
#  that represents the updated inventory. Note that the addedItems list
#  can contain multiples of the same item.

def addtoinventory(inventory, added_items):
    for i in added_items:
        if i in inventory:
            inventory[i] += 1
        else:
            inventory[i] = 1
    return inventory

franks_inventory = {'coin' : 1, 'potion' : 3, 'diamond' : 11}
dragons_loot = ['coin', 'potion', 'coin', 'coin', 'diamond', 'ruby']
wizards_loot = ['potion', 'potion', 'magic dust']
print(franks_inventory)
print(addtoinventory(franks_inventory, dragons_loot))
print(addtoinventory(franks_inventory, wizards_loot))

