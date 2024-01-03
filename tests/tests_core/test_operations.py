import pytest
from sequence import FibonacciNumbers


@pytest.mark.parametrize('sequence_a, sequence_b', [(FibonacciNumbers(), FibonacciNumbers())])
class TestAddition:

    def test_commutativity(self, sequence_a, sequence_b):
        print(sequence_a + sequence_b)
        print(sequence_b + sequence_a)
        assert sequence_a + sequence_b != sequence_b + sequence_a, (sequence_b + sequence_a).__repr__

    def test_something2(self, sequence_a, sequence_b):
        pass
