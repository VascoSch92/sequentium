from typing import List, Type

import pytest

from sequence.core.core import Sequence
from sequence.core.utils.exceptions import InfiniteSequenceError


class SequenceTestSuite:
    """
    Test suite for evaluating properties and behavior of sequences.

    Attributes:
        sequence (Type[Sequence]): The sequence to be tested.
        is_finite (bool): Indicates whether the sequence is finite.
        is_periodic (bool): Indicates whether the sequence is periodic.
        ground_truth (List[int]): The expected elements of the sequence.
        ground_truth_length (int): The expected length of the sequence.
    """

    sequence: Type[Sequence] = None
    sequence_name: str = None
    is_finite: bool = False
    is_periodic: bool = False
    ground_truth: List[int] = None
    ground_truth_length: int = None

    def test_sequence_name(self):
        """Test if the sequence's name matches the expected value."""
        if self.sequence.__str__() != self.sequence_name:
            raise ValueError(f'Expected: {self.sequence_name}. Got {self.sequence.__str__()}')

    def test_is_finite(self):
        """Test if the sequence's finiteness matches the expected value."""
        if self.sequence.is_finite != self.is_finite:
            raise ValueError

    def test_is_periodic(self):
        """Test if the sequence's periodicity matches the expected value."""
        if self.sequence.is_periodic != self.is_periodic:
            raise ValueError

    def test_len(self):
        """Test the length of the sequence, considering finiteness."""
        if self.sequence.is_finite:
            assert len(self.sequence) == self.ground_truth_length
        else:
            with pytest.raises(InfiniteSequenceError):
                len(self.sequence)

    def test_getitem(self):
        """Test if sequence elements match the expected ground truth."""
        for index, element in enumerate(self.ground_truth):
            if self.sequence[index] != element:
                raise ValueError(f'Expected element: {element} at index {index}, but got {self.sequence[index]}!')

    def test_contains(self):
        """Test if elements from the ground truth are correctly identified in the sequence."""
        for element in self.ground_truth:
            if (element in self.sequence) is False:
                raise ValueError(f'The expression ({element} in sequence) must be True, but it is not!')

    def test_not_contains(self):
        """Test if elements not in the ground truth are correctly identified as not in the sequence."""
        for element in range(len(self.ground_truth)):
            if element not in self.ground_truth and (element not in self.sequence) is False:
                raise ValueError(f'The expression ({element} in sequence) must be True, but it is not!')

    def test_as_list(self):
        """Test if the as_list method returns the expected subsequence for various start and stop indices."""
        for j in range(self.ground_truth_length - 1):
            for i in range(j, self.ground_truth_length):
                if self.sequence.as_list(start=j, stop=i) != self.ground_truth[j:i]:
                    raise Exception(
                        f'Expected: {self.ground_truth[j:i]}. Got {self.sequence.as_list(start=j, stop=i)}!'
                    )


class FiniteSequenceTestSuite(SequenceTestSuite):
    """Test suite for evaluating properties and behavior of finite sequences."""

    is_finite = True


class PeriodicSequenceTestSuite(SequenceTestSuite):
    """
    Test suite for evaluating properties and behavior of periodic sequences.

    Attributes:
        period_length (int): The expected period length of the sequence.
    """

    is_periodic = True
    period_length: int

    def test_is_periodic(self):
        """Test if the sequence's periodicity matches the expected value."""
        if self.sequence.is_periodic != self.is_periodic:
            raise ValueError

    def test_period(self):
        """Test if the sequence's period matches the expected period length."""
        if self.period_length != self.sequence.period:
            raise ValueError(f'Expected period: {self.period_length}, but got {self.sequence.period}!')
