from math import isqrt


def is_prime(number: int) -> bool:
    if number <= 3:
        return number > 1
    elif number % 2 == 0 or number % 3 == 0:
        return False
    else:
        for d in range(5, isqrt(number) + 1, 6):
            if number % d == 0 or number % (d + 2) == 0:
                return False
        return True
