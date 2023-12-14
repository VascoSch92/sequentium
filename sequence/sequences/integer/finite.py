from typing import List

from sequence.core.finite_type import Finite
from sequence.core.utils.validation import validate_positive_integer


class A001228(Finite):
    """Orders of sporadic simple groups (https://oeis.org/A001228)."""

    def __init__(self):
        super().__init__()
        self.sequence = [
            7920, 95040, 175560, 443520, 604800, 10200960, 44352000, 50232960, 244823040, 898128000, 4030387200,
            145926144000, 448345497600, 460815505920, 495766656000, 42305421312000, 64561751654400, 273030912000000,
            51765179004000000, 90745943887872000, 4089470473293004800, 4157776806543360000, 86775571046077562880,
            1255205709190661721292800, 4154781481226426191177580544000000,
            808017424794512875886459904961710757005754368000000000,
        ]

    def __str__(self):
        return 'orders of sporadic simple groups sequence'


class A003173(Finite):
    """Heegner numbers: imaginary quadratic fields with unique factorization (https://oeis.org/A003173)."""

    def __init__(self):
        super().__init__()
        self.sequence = [1, 2, 3, 7, 11, 19, 43, 67, 163]

    def __str__(self):
        return 'Heegner numbers'


HeegnerNumbers = A003173



class CollatzSequence(Finite):
    """
    Collatz sequence: the sequence of numbers involved in the Collatz conjecture
    (https://en.wikipedia.org/wiki/Collatz_conjecture)
    """
    def __init__(self, start_value: int):
        super().__init__()
        start_value = validate_positive_integer(integer=start_value)
        self.sequence = self.generate_cycle(value=start_value)

    def __str__(self):
        return 'Collatz sequence'

    @staticmethod
    def generate_cycle(value: int) -> List[int]:
        cycle = [value]

        while value != 1:
            value = value // 2 if value % 2 == 0 else 3 * value + 1
            cycle.append(value)

        return cycle


HailstoneSequence = CollatzSequence
WondrousNumbers = CollatzSequence
HailstoneNumbers = CollatzSequence
