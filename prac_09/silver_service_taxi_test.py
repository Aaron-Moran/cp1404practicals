"""
CP1404/CP5632 Practical - Test SilverServiceTaxi class.
"""

from silver_service_taxi import SilverServiceTaxi


def main():
    """Test SilverServiceTaxi fare calculation."""
    fancy_taxi = SilverServiceTaxi("Fancy Taxi", 100, 2)

    fancy_taxi.drive(18)
    fare = fancy_taxi.get_fare()

    print(fancy_taxi)
    print(f"Fare for 18 km trip: ${fare:.2f}")

    assert abs(fare - 48.80) < 0.01, "Fare calculation is incorrect"


if __name__ == "__main__":
    main()
