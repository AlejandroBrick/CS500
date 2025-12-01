# Author: Alejandro Ceballos
# Date: 11/30/2025

class ItemToPurchase:    
    def __init__(self, item_name="none", item_description="none", item_price=0, item_quantity=0):
        self.name = item_name
        self.description = item_description
        self.price = item_price
        self.quantity = item_quantity
        
    def print_item_cost(self):
        total_cost = self.price * self.quantity
        print(f"{self.name} - {self.quantity} @ ${self.price} = ${total_cost}")

class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, ItemToPurchase):
        self.cart_items.append(ItemToPurchase)

    def remove_item(self, ItemName):
        found = False
        for item in self.cart_items:
            if item.name == ItemName:
                self.cart_items.remove(item)
                found = True
                break
        if not found:
            print("Item not found in cart. Nothing removed.")

    def modify_item(self, ItemToPurchase):
        found = False
        for item in self.cart_items:
            if item.name == ItemToPurchase.name:
                if ItemToPurchase.description != "none":
                    item.description = ItemToPurchase.description
                if ItemToPurchase.price != 0:
                    item.price = ItemToPurchase.price
                if ItemToPurchase.quantity != 0:
                    item.quantity = ItemToPurchase.quantity
                found = True
                break
        if not found:
            print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        total_items = 0
        for item in self.cart_items:
            total_items += item.quantity
        return total_items

    def get_cost_of_cart(self):
        total_cost = 0
        for item in self.cart_items:
            total_cost += float(item.price) * int(item.quantity)
        return total_cost

    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        
        total_items = self.get_num_items_in_cart()
        
        if total_items > 0:
            print(f"Number of Items: {total_items}")
            
            for item in self.cart_items:
                per_item_total = float(item.price) * int(item.quantity)
                print(f"{item.name} {item.quantity} @ ${item.price} = ${per_item_total}")
            total_cost = self.get_cost_of_cart()
            
            print(f"Total: ${total_cost}")
        else:
            print("SHOPPING CART IS EMPTY")
            print()

    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        
        if self.get_num_items_in_cart() == 0:
            print("SHOPPING CART IS EMPTY")
            print()
            return
        
        for item in self.cart_items:
            print(f"{item.name}: {item.description}")
            
def print_menu(cart):
    while True:
        print("MENU")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit")
        choice = input("Choose an option: ")
        print()
        
        match choice:
            case 'q':
                break
            case 'o':
                print("OUTPUT SHOPPING CART")
                cart.print_total()
                print()
            case 'i':
                print("OUTPUT ITEMS' DESCRIPTIONS")
                cart.print_descriptions()
                print()
            case 'a':
                print("ADD ITEM TO CART")
                item_name = input("Enter the item name: ")
                item_description = input("Enter the item description: ")
                item_price = float(input("Enter the item price: "))
                item_quantity = int(input("Enter the item quantity: "))
                new_item = ItemToPurchase(item_name, item_description, item_price, item_quantity)
                cart.add_item(new_item)
                print()
            case 'r':
                print("REMOVE ITEM FROM CART")
                item_name = input("Enter name of item to remove: ")
                cart.remove_item(item_name)
                print()
            case 'c':
                print("CHANGE ITEM QUANTITY")
                item_name = input("Enter the item name: ")
                new_quantity = int(input("Enter the new quantity: "))
                modified_item = ItemToPurchase(item_name, "none", 0, new_quantity)
                cart.modify_item(modified_item)
                print()  
            case _:
                print("Invalid option, please try again.")
                print()
                
def main():
    # Get customer name and date
    customer_name = input("Enter customer's name: ")
    current_date = input("Enter today's date: ")
    print()
    
    print(f"Customer name: {customer_name}")
    print(f"Today's date: {current_date}")
    print()
    
    shopping_cart = ShoppingCart(customer_name, current_date)
  
    print_menu(shopping_cart)
    
if __name__ == "__main__":
    main()