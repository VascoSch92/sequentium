from math import isqrt

from sequence.core.infinite_type import PropertyDefined


class A000040(PropertyDefined):
    """ The prime numbers (https://oeis.org/A000040) """

    def __init__(self):
        super().__init__()

    def property(self, number: int) -> bool:
        return self.is_prime(number=number)

    @staticmethod
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


class PrimeNumbers(A000040):
    pass


class PositivePrimeNumbers(A000040):
    pass
