from typing import Any

from sequence.core.infinite_type import Explicit
from sequence.sequences.integer.property_defined_generalised_sequences import TypesOfPrimes


class IntegerSequance(Explicit):

    def __contains__(self, item):
        return True

    def formula(self, index: int) -> Any:
        return index


class A000040(TypesOfPrimes):
    """ The prime numbers (https://oeis.org/A000040) """

    def __init__(self):
        super().__init__(base_sequence=IntegerSequance)


class PrimeNumbers(A000040):
    pass


class PositivePrimeNumbers(A000040):
    pass
