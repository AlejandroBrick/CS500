# Author: Alejandro Ceballos
# Date: 11/30/2025

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
            total_cost += item.price * item.quantity
        return total_cost

    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        
        total_items = self.get_num_items_in_cart()
        
        if total_items > 0:
            print(f"Number of Items: {total_items}")
            
            for item in self.cart_items:
                per_item_total = item.price * item.quantity
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
            case 'i':
                print("OUTPUT ITEMS' DESCRIPTIONS")
                cart.print_descriptions()
            case 'a':
                print("Add item to cart - Functionality not yet implemented.")
                print()
            case 'r':
                print("Remove item from cart - Functionality not yet implemented.")
                print()
            case 'c':
                print("Change item quantity - Functionality not yet implemented.")
                print()  
            case _:
                print("Invalid option, please try again.")
                print()
                
def main():
    # Get customer name and date
    customer_name = input("Enter customer's name: ")
    current_date = input("Enter today's date: ")
    print()
    
    shopping_cart = ShoppingCart(customer_name, current_date)
  
    print_menu(shopping_cart)
    
if __name__ == "__main__":
    main()