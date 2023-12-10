from typing import Tuple, Any

from sequentium.core.infinite_type import Recursive, MonotonicIncreasing
from sequentium.core.utils.validation import validate_integer_tuple
from sequentium.sequences.integer.recursive_generalised_sequences import LucasSequenceU, LucasSequenceV


class A000032(LucasSequenceV):
    """ Lucas numbers (https://oeis.org/A000032). """

    def __init__(self):
        super().__init__(p=1, q=-1)

    def __str__(self):
        return 'the Lucas numbers'

    def __contains__(self, item: Any) -> bool:
        if item == 1:
            return True
        for element in self._as_generator():
            if element == item:
                return True
            if element > item:
                return False


LucasNumbers = A000032


class A000045(LucasSequenceU):
    """Fibonacci numbers (https://oeis.org/A000045)."""

    def __init__(self):
        super().__init__(p=1, q=-1)

    def __str__(self):
        return 'the Fibonacci numbers'


FibonacciNumbers = A000045
FibonacciSequence = A000045


class A000073(MonotonicIncreasing, Recursive):
    """Tribonacci numbers (https://oeis.org/A000073)."""

    def __init__(self, start_terms: Tuple[int, int, int] = None):
        super().__init__()

        if start_terms is None:
            self.start_terms = (0, 1, 0)
        else:
            validate_integer_tuple(tuple=start_terms, length=3)
            self.start_terms = start_terms

    def __str__(self):
        return 'the Tribonacci numbers'

    def formula(self, terms: Tuple[int, int, int]) -> Tuple[int, int, int]:
        return terms[1], terms[2], sum(terms)


TribonacciNumbers = A000073



