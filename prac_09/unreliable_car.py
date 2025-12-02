"""
CP1404/CP5632 Practical - UnreliableCar class.
"""

import random

from car import Car


class UnreliableCar(Car):
    """Specialised Car that sometimes does not drive as intended."""

    def __init__(self, name, fuel, reliability):
        """
        Initialise an UnreliableCar instance.

        name: str, name of the car
        fuel: int, amount of fuel
        reliability: float, percentage chance (0-100) that the car will drive
        """
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Attempt to drive the given distance."""
        random_chance = random.uniform(0, 100)
        if random_chance < self.reliability:
            return super().drive(distance)
        return 0