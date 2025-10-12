"""
CP1404/CP5632 Practical
Quick Picks
"""
import random

NUMBER_PER_PICK = 6
MIN_NUMBER = 1
MAX_NUMBER = 45

def main():
    """Ask how many quick picks to generate."""
    quick_pick_count = int(input("How many quick picks? "))
    while quick_pick_count < 1:
        print("Invalid input, enter 1 or more")
        quick_pick_count = int(input("How many quick picks? "))

    for _ in range(quick_pick_count):
        print(generate_quick_picks())

def generate_quick_picks():
    """Return one quick pick."""
    numbers = []
    while len(numbers) < NUMBER_PER_PICK:
        value = random.randint(MIN_NUMBER, MAX_NUMBER)
        numbers.append(value)
    numbers.sort()
    return numbers


main()