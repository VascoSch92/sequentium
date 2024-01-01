from math import isqrt
from typing import Generator, Any


def is_in_monotonic_increasing_generator(generator: Generator, item: Any) -> bool:
    """
    Check if the element 'item' is present in a monotonic increasing generator.

    Args:
        - generator (Generator)
        - item (Any): The item to be checked for presence in the generator
    """
    for element in generator:
        if element == item:
            return True
        if element > item:
            return False
    return False


def is_prime(number: int) -> bool:
    """
    Check if a given number is a prime number.

    Args:
        - number (int): The number to be checked.
    """
    if number <= 3:
        return number > 1
    if number % 2 == 0 or number % 3 == 0:
        return False

    return all(not (number % d == 0 or number % (d + 2) == 0) for d in range(5, isqrt(number) + 1, 6))
