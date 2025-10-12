"""
CP1404/CP5632 Practical
list_exercises.py
"""

NUMBER_COUNT = 5

def main():
    """Run numbers summary"""
    numbers = get_numbers(NUMBER_COUNT)
    display_numbers_summary(numbers)


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


main()