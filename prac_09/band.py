"""
CP1404/CP5632 Practical - Band class.
"""

class Band:
    """Band class that associates multiple musicians."""

    def __init__(self, name):
        """
        Initialise a Band instance.

        name: str, name of the band
        """
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of the Band and its musicians."""
        musicians_string = ", ".join(str(musician) for musician in self.musicians)
        return f"{self.name} ({musicians_string})"

    def add(self, musician):
        """Add a musician to the band."""
        self.musicians.append(musician)

    def play(self):
        """Return a string of each musician's play output, one per line."""
        return "\n".join(musician.play() for musician in self.musicians)