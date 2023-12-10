from sequentium.core.infinite_type import Explicit
from sequentium.sequences.integer.explicit_generalised_sequences import GeneralisedNexusNumbers


class A000027(Explicit):
    """The natural numbers (https://oeis.org/A000027)."""

    def __contains__(self, item):
        return True

    def __str__(self):
        return 'the natural numbers'

    def formula(self, index: int) -> int:
        return index


PositiveIntegers = A000027
NaturalNumbers = A000027


class A000326(Explicit):
    """Pentagonal numbers (https://oeis.org/A000326)."""

    def __contains__(self, item):
        if item <= 0:
            return True
        else:
            n = (1 + (1 + 24 * item) ** (1 / 2)) / 6
            return n == int(n)

    def __str__(self):
        return 'the pentagonal numbers'

    def formula(self, index: int) -> int:
        return index * (3 * index - 1) // 2


PentagonalNumbers = A000326


class A003215(GeneralisedNexusNumbers):
    """Hex (or centered hexagonal) numbers (https://oeis.org/A003215)."""

    def __init__(self):
        super().__init__()
        self.dimension = 2

    def __str__(self):
        return 'the hex numbers'

    def __contains__(self, item):
        if item <= 0:
            return False
        else:
            n = (3 + (12 * item - 3) ** (1 / 2)) / 6
            return n == int(n)


HexNumbers = A003215
CenteredHexagonalNumbers = A003215


class A005408(Explicit):
    """The odd numbers (https://oeis.org/A005408)."""

    def __contains__(self, item: int) -> bool:
        return item % 2 == 1

    def __str__(self):
        return 'the odd numbers'

    def formula(self, index: int) -> int:
        return 2*index + 1


OddNumebrs = A005408


class A033999(Explicit):
    """Sequence of powers of -1 (https://oeis.org/A033999)."""

    def __contains__(self, item):
        return item in {-1, 1}

    def __str__(self):
        return 'the sequence of powers of -1'

    def formula(self, index: int) -> int:
        return (-1)**index
