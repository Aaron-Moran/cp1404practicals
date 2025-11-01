"""
CP1404/CP5632 Practical - Guitar class.

Expected: 25 minutes
Actual: 24 minutes
"""

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
        return "{} ({}) : ${:,.2f}".format(self.name, self.year, self.cost)


    def get_age(self, current_year: int) -> int:
        """Return the guitar's age in years using the provided current_year."""
        return current_year - self.year


    def is_vintage(self, current_year: int) -> bool:
        """Return True if the guitar is vintage (>= VINTAGE_AGE years)."""
        return self.get_age(current_year) >= VINTAGE_AGE