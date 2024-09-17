# Shopping Cart System

class ShoppingCart:
    def __init__(self):
        self.items = []  # List to store cart items
    
    def add_item(self):
        """Add items to the shopping cart."""
        number_of_items = int(input("Enter the number of items to purchase: "))
        for i in range(number_of_items):
            item_name = input(f"Enter the name of item {i + 1}: ")
            item_price = float(input(f"Enter the price of item {i + 1}: "))
            item_quantity = int(input(f"Enter the quantity of item {i + 1}: "))
            item = {"name": item_name, "price": item_price, "quantity": item_quantity}
            self.items.append(item)
        print(f"{number_of_items} products added to the shopping cart.")
    
    def remove_item(self, item_name):
        """Remove an item from the shopping cart by name."""
        item_found = False
        for item in self.items:
            if item["name"].lower() == item_name.lower():
                self.items.remove(item)
                item_found = True
                print(f'Item "{item_name}" has been removed from the shopping cart.')
                break
        if not item_found:
            print(f'Item "{item_name}" was not found in the shopping cart.')
    
    def calculate_total(self):
        """Calculate and return the total cost of items in the shopping cart."""
        total = 0
        for item in self.items:
            total += item["price"] * item["quantity"]
        print(f"The total cost for your shopping cart is: ${total:.2f}")
        return total
    
    def view_cart(self):
        """View all items in the shopping cart."""
        if not self.items:
            print("Your shopping cart is empty.")
        else:
            print("Items in your shopping cart:")
            for item in self.items:
                print(f'{item["quantity"]} x {item["name"]} - ${item["price"]:.2f} each')
                

# Example usage
shopping_cart = ShoppingCart()

# Add items
shopping_cart.add_item()

# View items in the cart
shopping_cart.view_cart()

# Calculate total
shopping_cart.calculate_total()

# Remove an item from the cart
item_to_remove = input("Enter the name of the item to remove: ")
shopping_cart.remove_item(item_to_remove)

# View updated cart
shopping_cart.view_cart()

# Calculate total again after removing an item
shopping_cart.calculate_total()
