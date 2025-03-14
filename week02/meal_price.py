# This program calculates the total cost of a meal, including child and adult meals, tax, and an optional tip.
# It also allows users to add drinks or appetizers and calculates the correct change after payment.

def main():
    # Get meal details
    child_meal_price = float(input("Enter the price of a child's meal: $"))
    adult_meal_price = float(input("Enter the price of an adult's meal: $"))
    num_children = int(input("Enter the number of children: "))
    num_adults = int(input("Enter the number of adults: "))

    subtotal = (child_meal_price * num_children) + (adult_meal_price * num_adults)

    drinks_price = float(input("Enter the total cost of drinks: $"))
    appetizers_price = float(input("Enter the total cost of appetizers: $"))
    subtotal += drinks_price + appetizers_price

    sales_tax_rate = float(input("Enter the sales tax rate (as a percentage): "))
    sales_tax = subtotal * (sales_tax_rate / 100)

    tip_percentage = float(input("Enter tip percentage (enter 0 for no tip): "))
    tip_amount = subtotal * (tip_percentage / 100)

    total_price = subtotal + sales_tax + tip_amount

    print("\n--- Receipt ---")
    print(f"Meal Subtotal:   ${subtotal:.2f}")
    print(f"Sales Tax ({sales_tax_rate:.1f}%): ${sales_tax:.2f}")
    print(f"Tip ({tip_percentage:.1f}%):      ${tip_amount:.2f}")
    print("----------------------")
    print(f"Total Price:     ${total_price:.2f}")

    payment_amount = float(input("\nEnter payment amount: $"))
    change = payment_amount - total_price

    if change >= 0:
        print(f"Change:          ${change:.2f}")
    else:
        print(f"Amount Due:      ${-change:.2f}")

main()
