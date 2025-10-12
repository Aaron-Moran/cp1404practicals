"""
CP1404/CP5632 Practical
list_exercises.py
"""

NUMBER_COUNT = 5
AUTHORISED_USERNAMES = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45','BaseInterpreterInterface', 'BaseStdIn',
                        'Command', 'ExecState','InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

def main():
    """Run numbers summary, then username access check."""
    numbers = get_numbers(NUMBER_COUNT)
    display_numbers_summary(numbers)
    security_checker()

def get_numbers(count):
    """Prompt for 'count' numbers and return them as a list of floats."""
    numbers = []
    for i in range(count):
        number = float(input(f"Number {i + 1}: "))
        numbers.append(number)
    return numbers

def display_numbers_summary(numbers):
    """Display first/last/min/max/average for the given numbers."""
    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    average = sum(numbers) / len(numbers)
    print(f"The average of the numbers is {average:.1f}")


def security_checker():
    """Prompt for a username and report whether access is granted."""
    username = input("Username: ").strip()
    if username in AUTHORISED_USERNAMES:
        print("Access granted")
    else:
        print("Access denied")


main()