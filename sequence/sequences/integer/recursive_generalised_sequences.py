from sequence.core.infinite_type import Recursive, MonotonicIncreasing
from sequence.core.utils.validations import validate_integer_tuple, validate_positive_integer
from typing import Tuple


class LucasSequenceU(MonotonicIncreasing, Recursive):
    """ Lucas sequence U_n (https://en.wikipedia.org/wiki/Lucas_sequence) """

    def __init__(self, p: int, q: int):
        super().__init__()
        validate_positive_integer(integer=p)
        validate_positive_integer(integer=q)

        self.p, self.q = p, q
        self.start_terms = (0, 1)

    def formula(self, terms: Tuple[int, int]) -> Tuple[int, int]:
        return terms[1], self.p * terms[0] - self.q * terms[1]


class LucasSequenceV(LucasSequenceU):
    """ Lucase sequence V_n (https://en.wikipedia.org/wiki/Lucas_sequence) """

    def __init__(self):
        super().__init__()

