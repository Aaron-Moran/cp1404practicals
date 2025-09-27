"""
CP1404/CP5632 - Practical 2
Score menu program.
"""

MENU = """G - Get a valid score
P - Print result
S - Show stars
Q - Quit"""

MIN_SCORE = 0
MAX_SCORE = 100
PASSABLE_SCORE = 50
EXCELLENT_SCORE = 90

def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = float(input("Enter score: "))
        elif choice == "P":
            print(get_result(score))
        elif choice == "S":
            # TODO: STARS
        else:
            print("Invalid option!")
        print(MENU)
        choice = input(">>> ").upper()
    print("farewell")
