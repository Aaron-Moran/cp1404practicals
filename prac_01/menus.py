"""
CP1404/CP5632 - Practical
Menus
Display a menu with options and perform actions until the user quits.
"""

# Prepare menu options
MENU = """(H)ello
(G)oodbye
(Q)uit"""

# Ask the user for their name once at the start
get_name = input("Enter name: ")

# Show the menu and ask for the user's first choice
print(MENU)
get_choice = input(">>> ").upper()

# Keep looping until the user chooses "Q"
while get_choice != "Q":
    if get_choice == "H":
        # Say hello to the user
        print(f"Hello {get_name}")
    elif get_choice == "G":
        # Say goodbye to the user
        print(f"Goodbye {get_name}")
    else:
        # Handle invalid menu choice
        print("Invalid choice")
    # Show the menu again for the next choice
    print(MENU)
    get_choice = input(">>> ").upper()

print("Finished.")