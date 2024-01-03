from sequence.core.finite_type import Periodic
from sequence.core.utils.validation import validate_positive_integer


class ConstantSequence(Periodic):
    """
    The class represent a constant sequence of a given value

    Attributes:
        value (int): the values that the constant sequence is taking
    """
    sequence_name = 'value sequence'

    def __init__(self, value: int) -> None:
        super().__init__(_period=1)
        self.sequence = [validate_positive_integer(integer=value)]
