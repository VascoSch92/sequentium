from typing import Generator

from sequence.core.core import InfiniteType
from sequence.core.infinite_type import PropertyDefined
from sequence.core.utils.functions import is_prime


class TypesOfPrimes(PropertyDefined):
    """
    Class representing a sequence of prime numbers based on a given property.

    Attributes:
        base_sequence (InfiniteType): The base sequence used for filtering prime numbers.
    """

    def __init__(self, base_sequence: InfiniteType):
        super().__init__()
        self.base_sequence = base_sequence()

    def as_generator(self) -> Generator:
        number = 1
        while True:
            if self.property(number=number) and number in self.base_sequence:
                yield number
            number += 1

    def property(self, number: int) -> bool:
        return is_prime(number=number)
