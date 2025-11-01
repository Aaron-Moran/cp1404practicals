"""
CP1404/CP5632 Practical - ProgrammingLanguage class.

I treated the development of both Languages.py and programming_languages.py as a single timer.
so total time is in languages.py
"""


class ProgrammingLanguage:
    """Represent a programming language."""

    def __init__(self, name: str, typing: str, reflection: bool, year: int):
        """Initialise a ProgrammingLanguage.

        name: the language name, e.g., "Python"
        typing: "Static" or "Dynamic"
        reflection: True if language supports reflection
        year: first appeared year (e.g., 1991)
        """

        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year


    def is_dynamic(self) -> bool:
        """Return True if this language uses dynamic typing."""
        return self.typing == "Dynamic"


    def __str__(self) -> str:
        """Return string representation of ProgrammingLanguage."""
        return (f"{self.name}, {self.typing} Typing, "
                f"Reflection={self.reflection}, First appeared in {self.year}")
    pass
