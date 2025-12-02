"""
CP1404/CP5632 Practical - SilverServiceTaxi class.
"""

from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised Taxi with fanciness multiplier and flagfall charge."""

    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """
        Initialise a SilverServiceTaxi instance.

        name: str, name of the taxi
        fuel: int, amount of fuel
        fanciness: float, multiplier for price per km
        """
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        """Return string representation including flagfall information."""
        return (f"{super().__str__()} plus flagfall of "
                f"${self.flagfall:.2f}")

    def get_fare(self):
        """Return the price for the taxi trip including flagfall."""
        return super().get_fare() + self.flagfall
