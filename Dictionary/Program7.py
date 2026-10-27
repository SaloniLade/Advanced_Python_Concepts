# Write a program to develop an inventory system for a small store. Each product has a name and a quantity in stock. The system should allow you to:
# - Add new products with their quantities.
# - Update the quantity of an existing product.
# - Display the product with the highest stock.
# - Remove a product from the inventory once it is sold out (quantity reaches 0).
# - Display the total number of unique products in the inventory.
# Tasks:
# - Use a dictionary where the product names are the keys, and the quantities are the values.
# - Implement functions for adding, updating, removing, and analyzing inventory.



inventory = {}


def add_product(name, quantity):
    inventory[name] = quantity


def update_product(name, quantity):
    if name in inventory:
        inventory[name] = quantity


def remove_product(name):
    if name in inventory:
        del inventory[name]


add_product("Pen", 50)
add_product("Book", 20)

update_product("Pen", 70)

highest = max(inventory, key=inventory.get)

print("Inventory:", inventory)
print("Highest Stock:", highest)
print("Total Products:", len(inventory))