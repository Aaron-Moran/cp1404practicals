"""
CP1404/CP5632 Practical - Guitar class.
"""

CURRENT_YEAR = 2025
VINTAGE_AGE = 50

class Guitar:
    """Represents a guitar"""


    def __init__(self, name: str = "", year: int = 0, cost: float = 0.0):
        """Initialise a Guitar instance.

        name: str, name of the guitar
        year: int, year the guitar was made
        cost: float, price of the guitar
        """
        self.name = name
        self.year = year
        self.cost = cost


    def __str__(self) -> str:
        """Return string representation: 'Name (Year) : $X,XXX.XX'."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"


    def __lt__(self, other: "Guitar") -> bool:
        """Return True if this guitar is 'less than' another (older year)."""
        return self.year < other.year


    def get_age(self) -> int:
        """Return the guitar's age in years."""
        return CURRENT_YEAR - self.year


    def is_vintage(self) -> bool:
        """Return True if the guitar is vintage."""
        return self.get_age() >= VINTAGE_AGE