"""
CP1404/CP5632 - Practical
Shop Calculator
Compute the total price for a given number of items.
Apply a 10% discount if the total price exceeds $100.
"""

# Ask the user how many items they want to buy
number_of_items = int(input("Number of items: "))

# Validate input: number of items must be > 0
while number_of_items <= 0:
    print("Invalid number of items!")  # Error message for invalid input
    number_of_items = int(input("Number of items: "))

# Initialise accumulator for total price
total_price = 0

# Loop for each item to get its price and add to running total
for i in range(number_of_items):
    price_of_item = float(input("Price of item: "))
    total_price += price_of_item

# Apply 10% discount if the total price is greater than $100
if total_price > 100:
    total_price *= 0.9

# Display the final total price with 2 decimal places
print(f"Total price for {number_of_items} items is ${total_price:.2f}")
