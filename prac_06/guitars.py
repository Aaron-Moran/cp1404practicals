"""
CP1404/CP5632 Practical - Gather and display guitars using the Guitar class.

Expected: 20 minutes
Actual: 30 minutes? (I lost track of time with the output formating)
"""

from guitar import Guitar

CURRENT_YEAR = 2025

def main():
    """Collect guitars from the user (until blank name) then display them"""
    print("My guitars!")
    guitars = []

    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar} added.\n")
        name = input("Name: ")

    print("\nThese are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage(CURRENT_YEAR) else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")

if __name__ == "__main__":
    main()