def main():
    print("\nWelcome to the Shopping Cart Program!\n")
    
    cart_items = []
    
    while True:
        print("\nPlease select one of the following: ")
        print("1. Add item")
        print("2. View cart")
        print("3. Remove item")
        print("4. Compute total")
        print("5. Quit")
        
        action = input("Please enter an action: ")
        
        if action == "1":
            # Add item
            item = input("What item would you like to add? ")
            cart_items.append(item)
            print(f"'{item}' has been added to the cart.")
            
        elif action == "2":
            # View cart
            if not cart_items:
                print("The shopping cart is empty.")
            else:
                print("The contents of the shopping cart are:")
                for item in cart_items:
                    print(item)
                    
        elif action == "3":
            # Remove item (not implemented in milestone)
            print("This feature will be available in the final version.")
            
        elif action == "4":
            # Compute total (not implemented in milestone)
            print("This feature will be available in the final version.")
            
        elif action == "5":
            # Quit
            print("Thank you. Goodbye.")
            break
            
        else:
            print("Invalid selection. Please choose a number between 1-5.")

if __name__ == "__main__":
    main()