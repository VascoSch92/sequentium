from math import isqrt


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
