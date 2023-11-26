from sequence.sequences.integer.explicit import A000027
from sequence.sequences.integer.property_defined_generalised_sequences import TypesOfPrimes


class A000040(TypesOfPrimes):
    """ The prime numbers (https://oeis.org/A000040) """

    def __init__(self):
        super().__init__(base_sequence=A000027)


PrimeNumbers = A000040
PositivePrimeNumbers = A000040
