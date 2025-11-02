# Author: Alejandro Ceballos
# Date: 2025-11-2

# Step 1: Build the ItemToPurchase class with the following specifications:

#     Attributes
#     item_name (string)
#     item_price (float)
#     item_quantity (int)
#     Default constructor
#     Initializes item's name = "none", item's price = 0, item's quantity = 0
#     Method
#     print_item_cost()

# Step 2: In the main section of your code, prompt the user for two items and create two objects of the ItemToPurchase class.

# Step 3: Add the costs of the two items together and output the total cost.


class ItemToPurchase:    
    def __init__(self, item_name="none", item_price=0, item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        
    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity
        print(f"{self.item_name} - {self.item_quantity} @ ${self.item_price} = ${total_cost}")
        

# Get first item
name1 = input("Enter the item 1 name: ")
price1 = float(input("Enter the item 1 price: "))
quantity1 = int(input("Enter the item 1 quantity: "))

item1 = ItemToPurchase(name1, price1, quantity1)

print("\n")

# Get second item
name2 = input("Enter the item 2 name: ")
price2 = float(input("Enter the item 2 price: "))
quantity2 = int(input("Enter the item 2 quantity: "))

item2 = ItemToPurchase(name2, price2, quantity2)

#total cost
print("\n")
print("TOTAL COST", end="\n")
item1.print_item_cost()
item2.print_item_cost()

total_cost = (item1.item_price * item1.item_quantity) + (item2.item_price * item2.item_quantity)
print(f"\nTotal: ${total_cost}")
