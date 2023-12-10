from typing import Tuple

from sequentium.core.infinite_type import Recursive, MonotonicIncreasing
from sequentium.core.utils.validation import validate_integer


class LucasSequenceU(MonotonicIncreasing, Recursive):
    """
    The class generates the Lucas sequence U_n (https://en.wikipedia.org/wiki/Lucas_sequence).
    The sequence is defined by the recurrence relation: U_{n+2} = p * U_{n+1} - q * U_n,
    with initial terms (0, 1).

    Attributes:
        p (int): Coefficient for the U_{n+1} term.
        q (int): Coefficient for the U_n term.
    """

    def __init__(self, p: int, q: int):
        super().__init__(start_terms=(0, 1))
        self.p = validate_integer(integer=p)
        self.q = validate_integer(integer=q)

    def __str__(self):
        return 'Lucas sequence U_n'

    def formula(self, terms: Tuple[int, int]) -> Tuple[int, int]:
        return terms[1], self.p * terms[0] - self.q * terms[1]


class LucasSequenceV(LucasSequenceU):
    """
    The class extends LucasSequenceU and generates the Lucas sequence V_n
    (https://en.wikipedia.org/wiki/Lucas_sequence), a variant with different initial terms.
    The sequence is defined by the recurrence relation: V_{n+2} = p * V_{n+1} - q * V_n,
    with initial terms (2, p).

    Attributes:
        p (int): Coefficient for the V_{n+1} term.
        q (int): Coefficient for the V_n term.
    """

    def __init__(self, p: int, q:  int):
        super().__init__(p=p, q=q)

        self.start_terms = (2, self.p)

    def __str__(self):
        return 'Lucas sequence V_n'
