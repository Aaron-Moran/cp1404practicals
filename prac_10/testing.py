"""
CP1404/CP5632 Practical
Testing code using assert and doctest
"""

import doctest
from prac_06.car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return " ".join([s] * n)


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def phrase_to_sentence(phrase):
    """
    Format a phrase as a sentence, starting with a capital and ending with a full stop.
    >>> phrase_to_sentence('hello')
    'Hello.'
    >>> phrase_to_sentence('It is an ex parrot.')
    'It is an ex parrot.'
    >>> phrase_to_sentence('goodbye friend')
    'Goodbye friend.'
    """
    phrase = phrase.strip()
    if not phrase:
        return "."
    sentence = phrase[0].upper() + phrase[1:]
    if not sentence.endswith("."):
        sentence = sentence + "."
    return sentence


def run_tests():
    """Run the tests on the functions."""
    # assert test with no message - used to see if the function works properly
    assert repeat_string("Python", 1) == "Python"
    # the test below should fail
    assert repeat_string("hi", 2) == "hi hi"

    car = Car()
    assert car._odometer == 0, "Car does not set odometer correctly"

    # Test default fuel
    car = Car()
    assert car.fuel == 0, "Car does not set default fuel correctly"
    # Test given fuel
    car = Car(fuel=10)
    assert car.fuel == 10, "Car does not set given fuel correctly"

run_tests()

doctest.testmod()
