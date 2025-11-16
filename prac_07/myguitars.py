"""
CP1404/CP5632 Practical
Read guitars from CSV, store as Guitar objects, sort by year, and display once.
"""

from guitar import Guitar

FILENAME = "guitars.csv"


def main():
    """Load guitars, sort and display, collect new entries, and save all to CSV."""
    guitars = load_guitars(FILENAME)

    guitars.sort()
    print("Guitars:")
    display_guitars(guitars)

    print("\nAdd new guitars (blank name to finish):")
    add_new_guitars(guitars)

    save_guitars(FILENAME, guitars)
    print(f"\n{len(guitars)} guitars saved to {FILENAME}")


def load_guitars(filename: str) -> list[Guitar]:
    """Read 'Name,Year,Cost' CSV rows into a list of Guitar objects."""
    guitars: list[Guitar] = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        for line in in_file:
            line = line.strip()
            if not line:
                continue
            name_text, year_text, cost_text = line.split(",")
            guitars.append(Guitar(name_text.strip(), int(year_text), float(cost_text)))
    return guitars


def display_guitars(guitars: list[Guitar]) -> None:
    """Display guitars with numbering and vintage tag."""
    for i, guitar in enumerate(guitars, 1):
        vintage = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>25} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage}")


def add_new_guitars(guitars: list[Guitar]) -> None:
    """Prompt the user to enter new guitars and append to the list."""
    name = input("Name: ").strip()
    while name != "":
        year = get_valid_int("Year: ")
        cost = get_valid_float("Cost: $")
        guitars.append(Guitar(name, year, cost))
        print(f"{name} ({year}) : ${cost:,.2f} added.\n")
        name = input("Name: ").strip()


def save_guitars(filename: str, guitars: list[Guitar]) -> None:
    """Write all guitars to CSV in 'Name,Year,Cost' format."""
    with open(filename, "w", encoding="utf-8") as out_file:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)


def get_valid_int(prompt: str) -> int:
    """Get a valid integer from the user."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input; enter a valid integer.")


def get_valid_float(prompt: str) -> float:
    """Get a valid floating-point number from the user."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input; enter a valid number.")


if __name__ == "__main__":
    main()