from typing import Tuple

from sequence.core.infinite_type import Recursive, MonotonicIncreasing
from sequence.core.validations import validate_integer_tuple


class A000045(Recursive, MonotonicIncreasing):
    """ Fibonacci numbers (https://oeis.org/A000045) """

    def __init__(self, start_terms: Tuple[int, int] = None):
        super().__init__()

        if start_terms is None:
            self.start_terms = (0, 1)
        else:
            validate_integer_tuple(tuple=start_terms, length=2)
            self.start_terms = start_terms

    def formula(self, terms: Tuple[int, int]) -> Tuple[int, int]:
        return terms[1], terms[0] + terms[1]


class FibonacciNumbers(A000045):
    pass


class A000073(Recursive, MonotonicIncreasing):
    """ Tribonacci numbers (https://oeis.org/A000073) """

    def __init__(self, start_terms: Tuple[int, int, int] = None):
        super().__init__()

        if start_terms is None:
            self.start_terms = (0, 1, 0)
        else:
            validate_integer_tuple(tuple=start_terms, length=3)
            self.start_terms = start_terms

    def formula(self, terms: Tuple[int, int, int]) -> Tuple[int, int, int]:
        return terms[1], terms[2], sum(terms)


class TribonacciNumbers(A000073):
    pass
