from typing import Tuple, List

from sequencepy.base.sequence import Sequence


class A000045(Sequence):

    def __init__(self):
        super().__init__()
        self.formula_type = 'recursive'
        self.start_terms = (0, 1)

    def __contains__(self, item):
        # FIXME
        raise NotImplementedError

    def formula(self, terms: List[int]) -> Tuple:
        return terms[1], terms[0] + terms[1]


class Fibonacci(A000045):
    pass


class A000073(Sequence):

    def __init__(self):
        super().__init__()
        self.formula_type = 'recursive'
        self.start_terms = (0, 0, 1)

    def __contains__(self, item):
        sequence = self.list(end=item)
        return item in sequence

    def formula(self, terms: List[int]) -> Tuple:
        return terms[1], terms[2], sum(terms)


class Tribonacci(A000073):
    pass


class A000326(Sequence):

    def __init__(self):
        super().__init__()
        self.formula_type = 'explicit'

    def __contains__(self, item):
        sequence = self.list(end=item)
        return item in sequence

    def formula(self, index: int) -> int:
        return index * (3 * index - 1) // 2
