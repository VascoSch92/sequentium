from sequence.core.infinite_type import PropertyDefined
from sequence.core.utils.functions import is_prime


class A000040(PropertyDefined):
    """ The prime numbers (https://oeis.org/A000040) """

    def __init__(self):
        super().__init__()

    def property(self, number: int) -> bool:
        return is_prime(number=number)


class PrimeNumbers(A000040):
    pass


class PositivePrimeNumbers(A000040):
    pass
