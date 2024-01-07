from typing import Any

from sequence.core.infinite_type import Explicit
from sequence.core.mixin import MonotonicIncreasingMixin
from sequence.sequences.integer.explicit_generalised import GeneralisedNexusNumbers, PolygonalNumbers


class A000027(Explicit):
    """The natural numbers (https://oeis.org/A000027)."""
    sequence_name = 'natural numbers'

    def __contains__(self, item: Any) -> bool:
        return True

    def formula(self, index: int) -> int:
        return index


PositiveIntegers = A000027
NaturalNumbers = A000027


class A000217(PolygonalNumbers):
    """Triangular numbers (https://oeis.org/A000217)."""
    sequence_name = 'triangular numbers'

    def __init__(self) -> None:
        super().__init__(number_of_sides=3)


TriangularNumbers = A000217


class A000290(Explicit):
    """Square numbers (https://oeis.org/A000290)."""
    sequence_name = 'square numbers'

    def __contains__(self, item: Any) -> bool:
        return False if item < 0 else int(item ** (1/2)) == item ** (1/2)

    def formula(self, index: int) -> int:
        return index ** 2


SquareNumbers = A000290


class A000326(PolygonalNumbers):
    """Pentagonal numbers (https://oeis.org/A000326)."""
    sequence_name = 'pentagonal numbers'

    def __init__(self) -> None:
        super().__init__(number_of_sides=5)


PentagonalNumbers = A000326


class A000384(PolygonalNumbers):
    """Hexagonal numbers (https://oeis.org/A000384)."""
    sequence_name = 'hexagonal numbers'

    def __init__(self) -> None:
        super().__init__(number_of_sides=6)


HexagonalNumbers = A000384


class A000566(PolygonalNumbers):
    """Heptagonal numbers (https://oeis.org/A000566)"""
    sequence_name = 'heptagonal numbers'

    def __init__(self) -> None:
        super().__init__(number_of_sides=7)


HeptagonalNumbers = A000566


class A000567(PolygonalNumbers):
    """Octagonal numbers (https://oeis.org/A000567)"""
    sequence_name = 'octagonal numbers'

    def __init__(self) -> None:
        super().__init__(number_of_sides=8)


OctagonalNumbers = A000567


class A001045(MonotonicIncreasingMixin, Explicit):
    """Jacobsthal numbers (https://oeis.org/A001045)."""
    sequence_name = 'Jacobsthal numbers'

    def formula(self, index: int) -> int:
        return round(2 ** index / 3)


JacobsthalNumbers = A001045
JacobsthalSequence = A001045


class A001106(PolygonalNumbers):
    """Nonagonal numbers (https://oeis.org/A001106)"""
    sequence_name = 'nonagonal numbers'

    def __init__(self) -> None:
        super().__init__(number_of_sides=9)


NonagonalNumbers = A001106


class A001107(PolygonalNumbers):
    """Decagonal numbers (https://oeis.org/A001107)"""
    sequence_name = 'decagonal numbers'

    def __init__(self) -> None:
        super().__init__(number_of_sides=10)


DecagonalNumbers = A001107


class A003215(GeneralisedNexusNumbers):
    """Hex (or centered hexagonal) numbers (https://oeis.org/A003215)."""
    sequence_name = 'hex numbers'

    def __init__(self) -> None:
        super().__init__(dimension=2)

    def __contains__(self, item: Any) -> bool:
        if item <= 0:
            return False
        n = (3 + (12 * item - 3) ** (1 / 2)) / 6
        return n == int(n)


HexNumbers = A003215
CenteredHexagonalNumbers = A003215


class A005408(Explicit):
    """The odd numbers (https://oeis.org/A005408)."""
    sequence_name = 'odd numbers'

    def __contains__(self, item: Any) -> bool:
        return item % 2 == 1

    def formula(self, index: int) -> int:
        return 2 * index + 1


OddNumbers = A005408


class A014551(MonotonicIncreasingMixin, Explicit):
    """Jacobsthal-Lucas numbers (https://oeis.org/A014551)."""
    sequence_name = 'Jacobsthal-Lucas numbers'

    def __contains__(self, item: Any) -> bool:
        if item == 1:
            return True
        return super().__contains__(item=item)

    def formula(self, index: int) -> int:
        return 2**index + (-1)**index


JachobsthalLucasNumbers = A014551


class A033999(Explicit):
    """Sequence of powers of -1 (https://oeis.org/A033999)."""
    sequence_name = 'sequence of powers of -1'

    def __contains__(self, item: Any) -> bool:
        return item in {-1, 1}

    def formula(self, index: int) -> int:
        return (-1)**index


class A051624(PolygonalNumbers):
    """Dodecagonal numbers https://oeis.org/A051624)."""
    sequence_name = 'dodecagonal numbers'

    def __init__(self) -> None:
        super().__init__(number_of_sides=12)


DodecagonalNumbers = A051624


class A051682(PolygonalNumbers):
    """Hendecagonal numbers (https://oeis.org/A051682)."""
    sequence_name = 'hendecagonal numbers'

    def __init__(self) -> None:
        super().__init__(number_of_sides=11)


HendecagonalNumbers = A051682


class A051865(PolygonalNumbers):
    """Tridecagonal numbers (https://oeis.org/A051865)."""
    sequence_name = 'tridecagonal numbers'

    def __init__(self) -> None:
        super().__init__(number_of_sides=13)


TridecagonalNumbers = A051865


class A051866(PolygonalNumbers):
    """Tetradecagonal numbers (https://oeis.org/A051866)."""
    sequence_name = 'tetradecagonal numbers'

    def __init__(self) -> None:
        super().__init__(number_of_sides=14)


TetradecagonalNumbers = A051866


class A051867(PolygonalNumbers):
    """Pentadecagonal numbers (https://oeis.org/A051867)."""
    sequence_name = 'pentadecagonal numbers'

    def __init__(self) -> None:
        super().__init__(number_of_sides=15)


PentadecagonalNumbers = A051867


class A051868(PolygonalNumbers):
    """Hexadecagonal numbers (https://oeis.org/A051868)."""
    sequence_name = 'hexadecagonal numbers'

    def __init__(self) -> None:
        super().__init__(number_of_sides=16)


HexadecagonalNumbers = A051868


class A051869(PolygonalNumbers):
    """Heptadecagonal numbers (https://oeis.org/A051869)."""
    sequence_name = 'heptadecagonal numbers'

    def __init__(self) -> None:
        super().__init__(number_of_sides=17)


HeptadecagonalNumbers = A051869


class A051870(PolygonalNumbers):
    """Octadecagonal numbers (https://oeis.org/A051870)."""
    sequence_name = 'octadecagonal numbers'

    def __init__(self) -> None:
        super().__init__(number_of_sides=18)


OctadecagonalNumbers = A051870


class A051871(PolygonalNumbers):
    """Enneadecagonal numbers (https://oeis.org/A051871)."""
    sequence_name = 'enneadecagonal numbers'

    def __init__(self) -> None:
        super().__init__(number_of_sides=19)


EnneadecagonalNumbers = A051871


class A051872(PolygonalNumbers):
    """Icosagonal numbers (https://oeis.org/A051872)."""
    sequence_name = 'icosagonal numbers'

    def __init__(self) -> None:
        super().__init__(number_of_sides=20)


IcosagonalNumbers = A051872


class A051873(PolygonalNumbers):
    """Icosihenagonal numbers (https://oeis.org/A051873)."""
    sequence_name = 'icosihenagonal numbers'

    def __init__(self) -> None:
        super().__init__(number_of_sides=21)


IcosihenagonalNumbers = A051873


class A051874(PolygonalNumbers):
    """Icosidigonal numbers (https://oeis.org/A051874)."""
    sequence_name = 'icosidigonal numbers'

    def __init__(self) -> None:
        super().__init__(number_of_sides=22)


IcosidigonalNumbers = A051874


class A051875(PolygonalNumbers):
    """Icositrigonal numbers (https://oeis.org/A051875)."""
    sequence_name = 'icositrigonal numbers'

    def __init__(self) -> None:
        super().__init__(number_of_sides=23)


IcositrigonalNumbers = A051875


class A051876(PolygonalNumbers):
    """Icositetragonal numbers (https://oeis.org/A051876)."""
    sequence_name = 'icositetragonal numbers'

    def __init__(self) -> None:
        super().__init__(number_of_sides=24)


IcositetragonalNumbers = A051876


class A167149(PolygonalNumbers):
    """Myriagonal numbers (https://oeis.org/A167149)."""
    sequence_name = 'myriagonal numbers'

    def __init__(self) -> None:
        super().__init__(number_of_sides=10_000)


MyriagonalNumbers = A167149
