from typing import Tuple, Any

from sequence.core.infinite_type import Recursive
from sequence.core.mixin import MonotonicIncreasingMixin
from sequence.core.utils.validation import validate_integer, validate_positive_integer


class HighOrderFibonacciNumbers(MonotonicIncreasingMixin, Recursive):
    """
        Class for generating high order Fibonacci numbers (https://mathworld.wolfram.com/Fibonaccin-StepNumber.html).

        Attributes:
            order (int): The order of the Fibonacci sequence.
    """
    sequence_name = 'High order Fibonacci numbers'

    def __init__(self, order: int) -> None:
        self.order = validate_positive_integer(integer=order)
        start_terms = self._compute_start_terms()

        super().__init__(start_terms=start_terms)

    def _compute_start_terms(self) -> Tuple[Any, ...]:
        """
        The method gives a tuple representing the start terms of the Fibonacci sequence.
        The start terms are computed as following:
            If the Fibonacci sequence has order n, then the tuple has 0 in the n-1 first position and 1 in the last.
        """
        return (0,) * (self.order - 1) + (1,)

    def formula(self, terms: Tuple[Any, ...]) -> Tuple[Any, ...]:
        return *[terms[i] for i in range(1, self.order)], sum(terms)


class LucasSequenceU(MonotonicIncreasingMixin, Recursive):
    """
    The class generates the Lucas sequence U_n (https://en.wikipedia.org/wiki/Lucas_sequence).
    The sequence is defined by the recurrence relation: U_{n+2} = p * U_{n+1} - q * U_n,
    with initial terms (0, 1).

    Attributes:
        p (int): Coefficient for the U_{n+1} term.
        q (int): Coefficient for the U_n term.
    """
    sequence_name = 'Lucas sequence U_n'

    def __init__(self, p: int, q: int) -> None:
        super().__init__(start_terms=(0, 1))
        self.p = validate_integer(integer=p)
        self.q = validate_integer(integer=q)

    def formula(self, terms: Tuple[int, int]) -> Tuple[int, int]:
        return terms[1], self.p * terms[1] - self.q * terms[0]


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
    sequence_name = 'Lucas sequence V_n'

    def __init__(self, p: int, q:  int) -> None:
        super().__init__(p=p, q=q)

        self.start_terms = (2, self.p)
