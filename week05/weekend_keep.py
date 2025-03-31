def main():
    print("\nWelcome to the Shopping Cart Program!\n")
    
    items = []
    prices = []
    quantities = []
    
    while True:
        print("\nPlease select one of the following: ")
        print("1. Add item")
        print("2. View cart")
        print("3. Remove item")
        print("4. Compute total")
        print("5. Quit")
        print("6. Clear cart")  # Added creative feature
        
        action = input("Please enter an action: ").strip()
        
        if action == "1":
            # Add item with enhanced features
            item = input("What item would you like to add? ").strip()
            
            while True:
                try:
                    price = float(input(f"What is the price of '{item}'? $").strip())
                    if price <= 0:
                        print("Price must be positive. Please try again.")
                        continue
                    break
                except ValueError:
                    print("Invalid price. Please enter a number.")
            
            while True:
                try:
                    quantity = int(input(f"How many '{item}' would you like to add? ").strip())
                    if quantity <= 0:
                        print("Quantity must be positive. Please try again.")
                        continue
                    break
                except ValueError:
                    print("Invalid quantity. Please enter a whole number.")
            
            items.append(item)
            prices.append(price)
            quantities.append(quantity)
            print(f"{quantity} '{item}' has been added to the cart at ${price:.2f} each.")
            
        elif action == "2":
            # View cart with enhanced formatting
            if not items:
                print("The shopping cart is empty.")
            else:
                print("\nThe contents of the shopping cart are:")
                print("-" * 40)
                print(f"{'#':<4}{'Item':<20}{'Price':<10}{'Qty':<6}{'Subtotal':<10}")
                print("-" * 40)
                
                total = 0
                for i, (item, price, qty) in enumerate(zip(items, prices, quantities), 1):
                    subtotal = price * qty
                    total += subtotal
                    print(f"{i:<4}{item:<20}${price:<9.2f}{qty:<6}${subtotal:<9.2f}")
                
                print("-" * 40)
                print(f"{'Total:':<30}${total:.2f}")
                print("-" * 40)
                
        elif action == "3":
            # Remove item with validation
            if not items:
                print("The shopping cart is empty.")
                continue
                
            # Show cart contents
            print("\nThe contents of the shopping cart are:")
            for i, (item, price, qty) in enumerate(zip(items, prices, quantities), 1):
                print(f"{i}. {item} - ${price:.2f} (Qty: {qty})")
                
            while True:
                try:
                    choice = input("\nWhich item would you like to remove? (or 'cancel' to go back) ").strip()
                    if choice.lower() == 'cancel':
                        break
                    
                    index = int(choice) - 1
                    if 0 <= index < len(items):
                        removed_item = items.pop(index)
                        removed_price = prices.pop(index)
                        removed_qty = quantities.pop(index)
                        print(f"Removed {removed_qty} '{removed_item}' at ${removed_price:.2f} each.")
                        break
                    else:
                        print(f"Sorry, that is not a valid item number (1-{len(items)}).")
                except ValueError:
                    print("Please enter a valid number or 'cancel'.")
                    
        elif action == "4":
            # Compute total with enhanced display
            if not items:
                print("The shopping cart is empty.")
            else:
                total = sum(price * qty for price, qty in zip(prices, quantities))
                print(f"\nThe total price of {sum(quantities)} items in the shopping cart is ${total:.2f}")
                
        elif action == "5":
            # Quit
            print("\nThank you for using the shopping cart. Goodbye!")
            break
            
        elif action == "6":
            # Clear cart - added creative feature
            if not items:
                print("The shopping cart is already empty.")
            else:
                confirm = input("Are you sure you want to clear the entire cart? (yes/no): ").strip().lower()
                if confirm == 'yes':
                    items.clear()
                    prices.clear()
                    quantities.clear()
                    print("Shopping cart has been cleared.")
                else:
                    print("Cart clearance canceled.")
                    
        else:
            print("Invalid selection. Please choose a number between 1-6.")

if __name__ == "__main__":
    main()
    
# Final Features Implemented:
# Price Storage: Now stores prices along with item names in separate lists
# Quantity Tracking: Added ability to track quantities of each item (creative feature)
# Enhanced Display:
# Shows item numbers starting from 1
# Displays prices formatted to 2 decimal places with $ symbol
# Added quantity and subtotal columns
# Improved table formatting with borders
# Total Calculation: Computes and displays the total price of all items
# Item Removal:
# Properly removes both item name and price
# Validates user input
# Handles edge cases (first/last items)
# Clear Cart Option: Added option to empty the entire cart (creative feature)
# Input Validation:
# Validates price input (must be positive number)
# Validates quantity input (must be positive integer)
# Validates removal selection (must be within bounds)
# Additional Creative Features:
# Quantity Management: Users can specify how many of each item they want
# Enhanced Display Format: Professional-looking table with aligned columns
# Clear Cart Function: Option to empty the entire cart at once
# Subtotal Calculation: Shows subtotal for each line item
# Cancellation Option: Allows cancelling removal operation
# Confirmation Prompt: For clearing the cart
# The program now provides a complete shopping cart experience with robust features and improved user interface.    