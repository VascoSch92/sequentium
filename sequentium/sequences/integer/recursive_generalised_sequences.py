from typing import Tuple

from sequentium.core.infinite_type import Recursive, MonotonicIncreasing
from sequentium.core.utils.validation import validate_integer, validate_integer_tuple


class LucasSequenceU(MonotonicIncreasing, Recursive):
    """Lucas sequentium U_n (https://en.wikipedia.org/wiki/Lucas_sequence)."""

    def __init__(self, p: int, q: int):
        super().__init__(start_terms=(0, 1))
        validate_integer(integer=p)
        validate_integer(integer=q)
        validate_integer_tuple(tuple=self.start_terms, length=2)

        self.p, self.q = p, q

    def __str__(self):
        return 'the Lucas sequentium U_n'

    def formula(self, terms: Tuple[int, int]) -> Tuple[int, int]:
        return terms[1], self.p * terms[0] - self.q * terms[1]


class LucasSequenceV(LucasSequenceU):
    """Lucas sequentium V_n (https://en.wikipedia.org/wiki/Lucas_sequence)."""

    def __init__(self, p: int, q:  int):
        super().__init__(p=p, q=q)

        self.start_terms = (2, self.p)

    def __str__(self):
        return 'the Lucas sequentium V_n'
