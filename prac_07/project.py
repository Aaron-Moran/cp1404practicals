"""
CP1404/CP5632 Practical - Project class.
"""

from datetime import date


class Project:
    """Represent a project with core attributes."""


    def __init__(self, name: str, start_date: date, priority: int, estimate: float, completion: int):
        """
        Initialise a Project.

        name: str,
        start_date: int,
        priority: int,
        estimate: float,
        completion: int,
        """
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.estimate = estimate
        self.completion = completion


    def __lt__(self, other: "Project") -> bool:
        """Order projects by priority."""
        return self.priority < other.priority


    def is_complete(self) -> bool:
        """Return True if the project is completed (100%)."""
        return self.completion >= 100


    def starts_after(self, dt: date) -> bool:
        """Return True if project starts strictly after the given date."""
        return self.start_date > dt


    def __str__(self) -> str:
        """Return a single-line summary."""
        return (f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, "
                f"priority {self.priority}, estimate: ${self.estimate:,.2f}, "
                f"completion: {self.completion}%")