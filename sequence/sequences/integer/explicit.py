from sequence.core.infinite_type import Explicit
from sequence.core.infinite_type import MonotonicIncreasing
from sequence.sequences.integer.explicit_generalised_sequences import GeneralisedNexusNumbers, PolygonalNumbers


class A000027(Explicit):
    """The natural numbers (https://oeis.org/A000027)."""

    def __contains__(self, item):
        return True

    def __str__(self):
        return 'natural numbers'

    def formula(self, index: int) -> int:
        return index


PositiveIntegers = A000027
NaturalNumbers = A000027


class A000217(PolygonalNumbers):
    """Triangular numbers (https://oeis.org/A000217)."""
    def __init__(self):
        super().__init__(number_of_sides=3)

    def __str__(self):
        return 'triangular numbers'


TriangularNumbers = A000217


class A000290(Explicit):
    """Square numbers (https://oeis.org/A000290)."""
    def __str__(self):
        return 'square numbers'

    def __contains__(self, item):
        return False if item < 0 else int(item**(1/2)) == item**(1/2)

    def formula(self, index: int) -> int:
        return index**2


SquareNumbers = A000290


class A000326(PolygonalNumbers):
    """Pentagonal numbers (https://oeis.org/A000326)."""
    def __init__(self):
        super().__init__(number_of_sides=5)

    def __str__(self):
        return 'pentagonal numbers'


PentagonalNumbers = A000326


class A000384(PolygonalNumbers):
    """Hexagonal numbers (https://oeis.org/A000384)."""
    def __init__(self):
        super().__init__(number_of_sides=6)

    def __str__(self):
        return 'hexagonal numbers'


HexagonalNumbers = A000384


class A001045(MonotonicIncreasing, Explicit):
    """Jacobsthal numbers (https://oeis.org/A001045)."""

    def __str__(self):
        return 'Jacobsthal numbers'

    def formula(self, index: int) -> int:
        return round(2 ** index / 3)


JacobsthalNumbers = A001045
JacobsthalSequence = A001045


class A003215(GeneralisedNexusNumbers):
    """Hex (or centered hexagonal) numbers (https://oeis.org/A003215)."""

    def __init__(self):
        super().__init__(dimension=2)

    def __str__(self):
        return 'hex numbers'

    def __contains__(self, item):
        if item <= 0:
            return False

        n = (3 + (12 * item - 3) ** (1 / 2)) / 6
        return n == int(n)


HexNumbers = A003215
CenteredHexagonalNumbers = A003215


class A005408(Explicit):
    """The odd numbers (https://oeis.org/A005408)."""

    def __contains__(self, item: int) -> bool:
        return item % 2 == 1

    def __str__(self):
        return 'odd numbers'

    def formula(self, index: int) -> int:
        return 2 * index + 1


OddNumbers = A005408


class A014551(MonotonicIncreasing, Explicit):
    """Jacobsthal-Lucas numbers (https://oeis.org/A014551)."""

    def __contains__(self, item):
        if item == 1:
            return True
        return super().__contains__(item=item)

    def __str__(self):
        return 'Jacobsthal-Lucas numbers'

    def formula(self, index: int) -> int:
        return 2**index + (-1)**index


JachobsthalLucasNumbers = A014551


class A033999(Explicit):
    """Sequence of powers of -1 (https://oeis.org/A033999)."""

    def __contains__(self, item):
        return item in {-1, 1}

    def __str__(self):
        return 'sequence of powers of -1'

    def formula(self, index: int) -> int:
        return (-1)**index
