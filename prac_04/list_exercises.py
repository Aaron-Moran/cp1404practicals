"""
CP1404/CP5632 Practical
list_exercises.
"""

NUMBER_COUNT = 5

def main():
    """Prompt for numbers, store them, then display summary information."""
    numbers = []
    for _ in range(NUMBER_COUNT):
        number = float(input("Number: "))
        numbers.append(number)

    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    average = sum(numbers) / len(numbers)
    print(f"The average of the numbers is {average}")


main()