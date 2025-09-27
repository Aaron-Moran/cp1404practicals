"""
CP1404/CP5632 - Practical
Program to determine score status
"""

import random

MENU = """E - Evaluate a score
R - Generate a random score
Q - Quit """

MIN_SCORE = 0
MAX_SCORE = 100
PASSABLE_SCORE = 50
EXCELLENT_SCORE = 90

def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "E":
            score = float(input("Enter Score: "))
            print(get_result(score))
        elif choice == "R":
            score = get_random_score()
            print(f"Random score: {score}")
            print(get_result(score))
        else:
            print("invalid value")
        print(MENU)
        choice = input(">>> ").upper()
    print("Goodbye!")

def get_result(score):
    if score < MIN_SCORE or score > MAX_SCORE:
        return "Invalid score"
    elif score >= EXCELLENT_SCORE:
        return "Excellent"
    elif score >= PASSABLE_SCORE:
        return "Passable"
    else:
        return "Bad"

def get_random_score():
    return random.randint(MIN_SCORE, MAX_SCORE)

main()