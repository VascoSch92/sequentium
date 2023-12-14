from abc import ABC
from typing import Generator, Type

from sequence.core.core import Sequence
from sequence.core.infinite_type import PropertyDefined
from sequence.core.utils.functions import is_prime


class PrimesOfSequence(PropertyDefined, ABC):
    """
    The class generates a sequence of prime numbers based on a specified property
    by filtering numbers from a base sequence.

    Attributes:
        base_sequence (Type[Sequence]): The base sequence used for filtering prime numbers.
    """

    def __init__(self, base_sequence: Type[Sequence]):
        super().__init__()
        self.base_sequence = base_sequence()

    def _as_generator(self) -> Generator:
        number = 1
        while True:
            if self.property(number=number) and number in self.base_sequence:
                yield number
            number += 1

    def property(self, number: int) -> bool:
        return is_prime(number=number)
