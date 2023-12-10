from typing import Tuple, Any

from sequentium.core.infinite_type import Recursive, MonotonicIncreasing
from sequentium.core.utils.validation import validate_integer_tuple
from sequentium.sequences.integer.recursive_generalised_sequences import LucasSequenceU, LucasSequenceV


class A000032(LucasSequenceV):
    """Lucas numbers (https://oeis.org/A000032)."""

    def __init__(self):
        super().__init__(p=1, q=-1)

    def __str__(self):
        return 'Lucas numbers'

    def __contains__(self, item: Any) -> bool:
        if item == 1:
            return True
        else:
            return super().__contains__(item=item)


LucasNumbers = A000032


class A000045(LucasSequenceU):
    """Fibonacci numbers (https://oeis.org/A000045)."""

    def __init__(self):
        super().__init__(p=1, q=-1)

    def __str__(self):
        return 'Fibonacci numbers'


FibonacciNumbers = A000045
FibonacciSequence = A000045


class A000073(MonotonicIncreasing, Recursive):
    """Tribonacci numbers (https://oeis.org/A000073)."""

    def __init__(self, start_terms: Tuple[int, int, int] = None):
        super().__init__()

        # TODO: fix here because probably this is not the case. i.e., we have a generelised sequence and then here fixe start terms
        if start_terms is None:
            self.start_terms = (0, 1, 0)
        else:
            validate_integer_tuple(tuple=start_terms, length=3)
            self.start_terms = start_terms

    def __str__(self):
        return 'Tribonacci numbers'

    def formula(self, terms: Tuple[int, int, int]) -> Tuple[int, int, int]:
        return terms[1], terms[2], sum(terms)


TribonacciNumbers = A000073


class A000129(LucasSequenceU):
    """Pell numbers (https://oeis.org/A000129)."""

    def __init__(self):
        super().__init__(p=2, q=-1)

    def __str__(self):
        return 'Pell numbers'


PellNumbers = A000129
LambdaNumbers = A000129


class A002203(LucasSequenceV):
    """Companion Pell numbers (https://oeis.org/A002203)."""
    def __init__(self):
        super().__init__(p=2, q=-1)

    def __str__(self):
        return 'Companion Pell numbers'


CompanionPellNumbers = A002203


class A214733(LucasSequenceU):
    """Sequence A214733 (https://oeis.org/A214733)."""

    def __init__(self):
        super().__init__(p=-1, q=3)

    def __str__(self):
        return 'sequence A214733'

    def __contains__(self, item):
        if item == 0:
            return True
        for element in self._as_generator():
            if element == item:
                return True
            if abs(element) > abs(item * 1_000):
                return False
