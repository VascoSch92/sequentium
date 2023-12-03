from sequence.sequences.integer.explicit import A000027
from sequence.sequences.integer.property_defined_generalised_sequences import TypesOfPrimes
from sequence.core.infinite_type import PropertyDefined
from sequence.core.utils.functions import is_prime


class A000040(TypesOfPrimes):
    """ The prime numbers (https://oeis.org/A000040)."""

    def __init__(self):
        super().__init__(base_sequence=A000027)

    def __str__(self):
        return 'the prime numbers'


PrimeNumbers = A000040
PositivePrimeNumbers = A000040


class A002808(PropertyDefined):
    """The composite numbers (https://oeis.org/A002808)."""

    def __init__(self):
        super().__init__()

    def property(self, number: int) -> bool:
        if number <= 3:
            return False
        return is_prime(number=number) is False

    def __str__(self):
        return 'the composite numbers'


CompositeNumbers = A002808
PositiveCompositeNumbers = A002808


