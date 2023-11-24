from sequence.core.infinite_type import Explicit
from sequence.sequences.integer.explicit_generalised_sequences import GeneralisedNexusNumbers


class A000027(Explicit):
    """ The natural numbers (https://oeis.org/A000027) """

    def __contains__(self, item):
        return True

    def formula(self, index: int) -> int:
        return index


class A000326(Explicit):
    """ Pentagonal numbers (https://oeis.org/A000326) """

    def __contains__(self, item):
        if item <= 0:
            return True
        else:
            n = (1 + (1 + 24 * item) ** (1 / 2)) / 6
            return n == int(n)

    def formula(self, index: int) -> int:
        return index * (3 * index - 1) // 2


class PentagonalNumbers(A000326):
    pass


class A003215(GeneralisedNexusNumbers):
    """ Hex (or centered hexagonal) numbers https://oeis.org/A003215 """

    def __init__(self):
        super().__init__()
        self.dimension = 2

    def __contains__(self, item):
        if item <= 0:
            return False
        else:
            n = (3 + (12 * item - 3) ** (1 / 2)) / 6
            return n == int(n)


class HexNumbers(A003215):
    pass


class CenteredHexagonalNumbers(A003215):
    pass


class A005408(GeneralisedNexusNumbers):
    """ The odd numbers (https://oeis.org/A005408) """

    def __init__(self):
        super().__init__()
        self.dimension = 1

    def __contains__(self, item: int) -> bool:
        return item % 2 == 1


class OddNumbers(A005408):
    pass
