from abc import ABC
from typing import Any, Union

from sequence.core.core_mixin import SequenceMixin
from sequence.core.operations import AddSequences, AddSequenceAndConstant


class Sequence(SequenceMixin, ABC):
    """Abstract base class for representing mathematical sequences."""
    sequence_name: str

    def __add__(self, other):
        if isinstance(other, Sequence):
            return AddSequences(sequence_a=self, sequence_b=other)
        if isinstance(other, Union[float, int]):
            return AddSequenceAndConstant(sequence=self, constant=other)

    def __eq__(self, other: Any) -> bool:
        """
        The method checks if the representation of the sequence is the same.
        It doesn't check that two sequences are equal, but that two sequences are different instance of the same class.
        """
        return other.__str__() == self.__str__() and other.__dict__ == self.__dict__

    def __str__(self) -> str:
        return self.sequence_name
