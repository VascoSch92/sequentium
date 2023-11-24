from typing import Tuple

from sequence.core.infinite_type import Recursive, MonotonicIncreasing
from sequence.core.utils.validations import validate_integer_tuple

class A000032(LucasSequenceV):
    """ Lucas numbers (https://oeis.org/A000032) """

    def __init__(self):
        super().__init__(p=1, q=-1)

    def __contains__(self, item: Any) -> bool:
        if item == 1:
            return True

        for element in self.as_generator():
            if element == item:
                return True
            if element > item:
                return False


class A000045(LucasSequenceU):
    """ Fibonacci numbers (https://oeis.org/A000045) """

    def __init__(self):
        super().__init__(p=1, q=-1)



class FibonacciNumbers(A000045):
    pass


class A000073(MonotonicIncreasing, Recursive):
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
