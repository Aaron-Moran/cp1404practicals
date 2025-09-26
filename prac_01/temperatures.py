"""
CP1404/CP5632 - Practical
Temperature Conversion Program
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""

print(MENU)
get_choice = input(">>> ").upper()
while get_choice != "Q":
    if get_choice == "C":
        # Convert Celsius to Fahrenheit
        celsius = float(input("Celsius: "))
        fahrenheit = celsius * 9.0 / 5 + 32
        print(f"Result: {fahrenheit:.2f} F")
    elif get_choice == "F":
        # Convert Fahrenheit to Celsius
        fahrenheit = float(input("Fahrenheit: "))
        celsius = 5 / 9 * (fahrenheit - 32)
        print(f"Result: {celsius:.2f} C")
    else:
        # Handle invalid menu choice
        print("Invalid option")

    print(MENU)
    get_choice = input(">>> ").upper()

print("Thank you.")