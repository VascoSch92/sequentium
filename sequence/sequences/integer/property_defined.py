from sequence.core.infinite_type import PropertyDefined
from sequence.core.utils.functions import is_prime
from sequence.sequences.integer.explicit import A000027
from sequence.sequences.integer.property_defined_generalised import PrimesOfSequence


class A000040(PrimesOfSequence):
    """ The prime numbers (https://oeis.org/A000040)."""
    sequence_name = 'prime numbers'

    def __init__(self) -> None:
        super().__init__(base_sequence=A000027)


PrimeNumbers = A000040
PositivePrimeNumbers = A000040


class A002808(PropertyDefined):
    """The composite numbers (https://oeis.org/A002808)."""
    sequence_name = 'composite numbers'

    def __init__(self) -> None:
        super().__init__()

    def property(self, number: int) -> bool:
        if number <= 3:
            return False
        return is_prime(number=number) is False


CompositeNumbers = A002808
PositiveCompositeNumbers = A002808
