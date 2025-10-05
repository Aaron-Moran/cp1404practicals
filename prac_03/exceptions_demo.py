"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

# Adjusted code to reprompt the user if the denominator is 0
try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
except ValueError:
    print("Numerator and denominator must be valid numbers!")
else:
    if denominator == 0:
        print("Cannot divide by zero!")
    else:
        fraction = numerator / denominator
        print(fraction)

print("Finished.")

# When will a ValueError occur?
# When the value cannot be converted to an int for either the numerator or the denominator, such as: 0.5 or 'a'

# When will a ZeroDivisionError occur?
# When the denominator is 0.

# Could you change the code to avoid the possibility of a ZeroDivisionError?
# You could add in a reprompt to request a different denominator if the denominator is 0.