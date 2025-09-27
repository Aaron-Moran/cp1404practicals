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

# Main loop to receive users input
def main():
    score = get_valid_score(MIN_SCORE, MAX_SCORE)
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score(MIN_SCORE, MAX_SCORE)
        elif choice == "P":
            print(get_result(score))
        elif choice == "S":
            show_stars(score)
        else:
            print("Invalid option!")
        print(MENU)
        choice = input(">>> ").upper()
    print("Farewell!")

# Applies a grade to the score
def get_result(score):
    if score >= EXCELLENT_SCORE:
        return "Excellent"
    elif score >= PASSABLE_SCORE:
        return "Passable"
    else:
        return "Bad"

# Gets a score from the user within the range of 0 - 100
def get_valid_score(min_score, max_score):
    score = float(input("Enter score: "))
    while score < min_score or score > max_score:
        print(f"invalid score. Input value between {min_score} and {max_score}.")
        score = float(input("Enter score: "))
    return score

# Prints a star (*) up to the value of the score
def show_stars(score):
    print("*" * int(score))

main()