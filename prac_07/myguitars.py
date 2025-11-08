"""
CP1404/CP5632 Practical
Read guitars from CSV, store as Guitar objects, sort by year, and display once.
"""

from guitar import Guitar

FILENAME = "guitars.csv"


def main():
    """Load guitars, sort from oldest to newest, and display them."""
    guitars = load_guitars(FILENAME)
    guitars.sort()
    print("Guitars:")
    display_guitars(guitars)


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
        print(f"{i}) {guitar}{vintage}")


if __name__ == "__main__":
    main()