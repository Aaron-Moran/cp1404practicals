"""
CP1404/CP5632 Practical - Test UnreliableCar class.
"""

from unreliable_car import UnreliableCar


def main():
    """Test UnreliableCar over many drive attempts."""
    reliable_car = UnreliableCar("Mostly reliable", 100, 90)
    unreliable_car = UnreliableCar("Dodgy", 100, 30)

    print("Testing UnreliableCar:")
    for attempt in range(1, 11):
        print(f"Attempt {attempt}:")
        print(f"{reliable_car.name} drove {reliable_car.drive(10)}km")
        print(f"{unreliable_car.name} drove {unreliable_car.drive(10)}km")
        print()

    print("Final states:")
    print(reliable_car)
    print(unreliable_car)


if __name__ == "__main__":
    main()
