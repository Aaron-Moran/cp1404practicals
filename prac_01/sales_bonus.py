"""
CP1404/CP5632 - Practical
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

# Ask the user for the initial sales amount
get_sales = float(input("Enter sales: $"))

# Continue calculating bonuses while the user enters a non-negative sales value
while get_sales >= 0:
    if get_sales >= 1000:
        # Apply 15% bonus for sales of $1000 or more
        sales_bonus = get_sales * 0.15
    elif get_sales < 1000:
        # Apply 10% bonus for sales below $1000
        sales_bonus = get_sales * 0.10
    else:
        # This case should not occur because of the while condition
        print("Invalid value")

    # Display the bonus formatted to 2 decimal places
    print(f"Sales bonus: ${sales_bonus:.2f}")

    # Ask for the next sales amount
    get_sales = float(input("Enter sales: $"))