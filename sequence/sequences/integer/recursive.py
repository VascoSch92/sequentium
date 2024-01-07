from typing import Any, Tuple, List, ClassVar
from sequence.core.mixin import AlmostMonotonicIncreasingMixin
from sequence.core.infinite_type import Recursive
from sequence.sequences.integer.recursive_generalised import (
    HighOrderFibonacciNumbers,
    LucasSequenceU,
    LucasSequenceV,
)


class A000032(LucasSequenceV):
    """Lucas numbers (https://oeis.org/A000032)."""
    sequence_name = 'Lucas numbers'

    def __init__(self) -> None:
        super().__init__(p=1, q=-1)

    def __contains__(self, item: Any) -> bool:
        if item == 1:
            return True
        return super().__contains__(item=item)


LucasNumbers = A000032


class A000045(LucasSequenceU):
    """Fibonacci numbers (https://oeis.org/A000045)."""
    sequence_name = 'Fibonacci numbers'

    def __init__(self) -> None:
        super().__init__(p=1, q=-1)


FibonacciNumbers = A000045
FibonacciSequence = A000045


class A000073(HighOrderFibonacciNumbers):
    """Tribonacci numbers (https://oeis.org/A000073)."""
    sequence_name = 'Tribonacci numbers'

    def __init__(self) -> None:
        super().__init__(order=3)


TribonacciNumbers = A000073


class A000078(HighOrderFibonacciNumbers):
    """Tetranacci numbers (https://oeis.org/A000078)."""
    sequence_name = 'Tetranacci numbers'

    def __init__(self) -> None:
        super().__init__(order=4)


TetranacciNumbers = A000078


class A000129(LucasSequenceU):
    """Pell numbers (https://oeis.org/A000129)."""
    sequence_name = 'Pell numbers'

    def __init__(self) -> None:
        super().__init__(p=2, q=-1)


PellNumbers = A000129
LambdaNumbers = A000129


class A000931(AlmostMonotonicIncreasingMixin, Recursive):
    """Padovan numbers (https://oeis.org/A000931)"""
    sequence_name = 'Padovan numbers'
    offset: ClassVar[List[int]] = [1, 0, 0, 1, 0, 1]

    def __init__(self) -> None:
        super().__init__(start_terms=(1, 0, 0))

    def formula(self, terms: Tuple[Any, ...]) -> Tuple[Any, ...]:
        return terms[1], terms[2], terms[1] + terms[0]


PadovanNumbers = A000931
PadovanSequence = A000931


class A001591(HighOrderFibonacciNumbers):
    """Pentanacci numbers (https://oeis.org/A001591)."""
    sequence_name = 'Pentanacci numbers'

    def __init__(self) -> None:
        super().__init__(order=5)


PentanacciNumbers = A001591


class A001592(HighOrderFibonacciNumbers):
    """Hexanacci numbers (https://oeis.org/A001592)."""
    sequence_name = 'Hexanacci numbers'

    def __init__(self) -> None:
        super().__init__(order=6)


HexanacciNumbers = A001591


class A001608(AlmostMonotonicIncreasingMixin, Recursive):
    """Perrin numbers (https://oeis.org/A001608)."""
    sequence_name = 'Perrin numbers'
    offset: ClassVar[List[int]] = [3, 0, 2, 3, 2, 5]

    def __init__(self) -> None:
        super().__init__(start_terms=(3, 0, 2))

    def formula(self, terms: Tuple[Any, ...]) -> Tuple[Any, ...]:
        return terms[1], terms[2], terms[1] + terms[0]


PerrinNumbers = A001608

class A002203(LucasSequenceV):
    """Companion Pell numbers (https://oeis.org/A002203)."""
    sequence_name = 'Companion Pell numbers'

    def __init__(self) -> None:
        super().__init__(p=2, q=-1)


CompanionPellNumbers = A002203
PellLucasNumbers = A002203


class A079262(HighOrderFibonacciNumbers):
    """Octanacci numbers (https://oeis.org/A079262)."""
    sequence_name = 'Octanacci numbers'

    def __init__(self) -> None:
        super().__init__(order=8)


OctanacciNumbers = A079262


class A104144(HighOrderFibonacciNumbers):
    """Enneanacci numbers (https://oeis.org/A104144)."""
    sequence_name = 'Enneanacci numbers'

    def __init__(self) -> None:
        super().__init__(order=9)


EnneanacciNumebrs = A104144


class A122189(HighOrderFibonacciNumbers):
    """Heptanacci numbers (https://oeis.org/A122189)."""
    sequence_name = 'Heptanacci numbers'

    def __init__(self) -> None:
        super().__init__(order=7)


HeptanacciNumbers = A122189


class A214733(LucasSequenceU):
    """Sequence A214733 (https://oeis.org/A214733)."""
    sequence_name = 'sequence A214733'

    def __init__(self) -> None:
        super().__init__(p=-1, q=3)

    def __contains__(self, item: Any) -> bool:
        if item == 0:
            return True
        for element in self._as_generator():
            if element == item:
                return True
            if abs(element) > abs(item * 1_000):
                return False
        return False
