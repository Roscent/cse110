# End of week02 Meal Price Calculator
# This program calculates the total cost of a meal, including sales tax, optional extras, and a tip.
# It also allows users to select a currency and provides change after payment.

def main():
    # Select your country's currency
    currency = input("Enter currency symbol (e.g., $, €, £, #): ").strip()

    child_meal_price = float(input(f"Enter the price of a child's meal ({currency}): "))
    adult_meal_price = float(input(f"Enter the price of an adult's meal ({currency}): "))
    num_children = int(input("Enter the number of children: "))
    num_adults = int(input("Enter the number of adults: "))

    subtotal = (child_meal_price * num_children) + (adult_meal_price * num_adults)

    drinks_price = float(input(f"Enter the total cost of drinks ({currency}): "))
    appetizers_price = float(input(f"Enter the total cost of appetizers ({currency}): "))
    subtotal += drinks_price + appetizers_price

    sales_tax_rate = float(input("Enter the sales tax rate (as a percentage): "))
    sales_tax = subtotal * (sales_tax_rate / 100)

    tip_percentage = float(input("Enter tip percentage (enter 0 for no tip): "))
    tip_amount = subtotal * (tip_percentage / 100)

    total_price = subtotal + sales_tax + tip_amount

    print("\n--- Receipt ---")
    print(f"Meal Subtotal:   {currency}{subtotal:.2f}")
    print(f"Sales Tax ({sales_tax_rate:.1f}%): {currency}{sales_tax:.2f}")
    print(f"Tip ({tip_percentage:.1f}%):      {currency}{tip_amount:.2f}")
    print("----------------------")
    print(f"Total Price:     {currency}{total_price:.2f}")

    payment_amount = float(input(f"\nEnter payment amount ({currency}): "))
    change = payment_amount - total_price

    if change >= 0:
        print(f"Change:          {currency}{change:.2f}")
    else:
        print(f"Amount Due:      {currency}{-change:.2f}")

main()
