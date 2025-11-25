"""
CP1404/CP5632 Practical - Taxi simulator.
"""

from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    """Run the taxi simulator program."""
    print("Let's drive!")
    taxis = [
        Taxi("Prius", 100),
        SilverServiceTaxi("Limo", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4)
    ]
    bill_to_date = 0.0
    current_taxi = None

    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "c":
            new_taxi = choose_taxi(taxis)
            if new_taxi is not None:
                current_taxi = new_taxi
        elif choice == "d":
            trip_cost = drive_taxi(current_taxi)
            bill_to_date += trip_cost
        else:
            print("Invalid option")

        print(f"Bill to date: ${bill_to_date:.2f}")
        print(MENU)
        choice = input(">>> ").lower()

    print(f"Total trip cost: ${bill_to_date:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)


def choose_taxi(taxis):
    """Let the user choose a taxi from the list and return it."""
    print("Taxis available:")
    display_taxis(taxis)
    try:
        taxi_choice = int(input("Choose taxi: "))
        if 0 <= taxi_choice < len(taxis):
            return taxis[taxi_choice]
        print("Invalid taxi choice")
    except ValueError:
        print("Invalid taxi choice")
    return None


def drive_taxi(current_taxi):
    """Drive the current taxi and return the trip cost."""
    if current_taxi is None:
        print("You need to choose a taxi before you can drive")
        return 0.0
    try:
        distance = float(input("Drive how far? "))
    except ValueError:
        distance = 0.0

    current_taxi.start_fare()
    current_taxi.drive(distance)
    trip_cost = current_taxi.get_fare()
    print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
    return trip_cost


def display_taxis(taxis):
    """Display the list of taxis with their index. """
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


if __name__ == "__main__":
    main()
