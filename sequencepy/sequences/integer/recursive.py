from typing import Tuple

from sequencepy.base.sequence import Recursive, MonotonlyIncreasing


class A000045(Recursive, MonotonlyIncreasing):
    """ Fibonacci numbers (https://oeis.org/A000045) """

    def __init__(self):
        super().__init__()
        self.start_terms = (0, 1)

    def formula(self, terms: Tuple[int, int]) -> Tuple[int, int]:
        return terms[1], terms[0] + terms[1]


class FibonacciNumbers(A000045):
    pass


class A000073(Recursive, MonotonlyIncreasing):
    """ Tribonacci numbers (https://oeis.org/A000073) """

    def __init__(self):
        super().__init__()
        self.start_terms = (0, 1, 0)

    def formula(self, terms: Tuple[int, int, int]) -> Tuple[int, int, int]:
        return terms[1], terms[2], sum(terms)


class TribonacciNumbers(A000073):
    pass
