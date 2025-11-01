"""
CP1404/CP5632 Practical - Manual tests for the Guitar class.

Expected: 10 minutes
Actual: 15 minutes
"""

from guitar import Guitar

CURRENT_YEAR = 2025

def main():
    """Test get_age and is_vintage with clear Expected/Got output."""
    l5 = Guitar("Gibson l-5 CES", 1922,16035.40)
    another = Guitar("Another Guitar", 2013, 0)

    expected_l5_age = CURRENT_YEAR - 1922
    expected_another_age = CURRENT_YEAR - 2013

    print(f"{l5.name} get_age() - Expected {expected_l5_age}. Got {l5.get_age(CURRENT_YEAR)}")
    print(f"{another.name} get_age() - Expected {expected_another_age}. Got {another.get_age(CURRENT_YEAR)}")

    print(f"{l5.name} is_vintage() -  Expected {expected_l5_age >= 50}, got {l5.is_vintage(CURRENT_YEAR)}")
    print(f"{another.name} is_vintage() -  Expected {expected_another_age >= 50}, got {another.is_vintage(CURRENT_YEAR)}")

if __name__ == "__main__":
    main()