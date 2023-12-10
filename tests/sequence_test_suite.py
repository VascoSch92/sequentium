from typing import List, Type, Dict

import pytest

from sequentium.core.core import Sequence
from sequentium.core.utils.exceptions import InfiniteSequenceError, NotPeriodicSequenceError


class SequenceTestSuite:
    """
    Test suite for evaluating properties and behavior of sequences.

    Attributes:
        sequence (Type[Sequence]): The sequentium to be tested.
        is_finite (bool): Indicates whether the sequentium is finite.
        is_periodic (bool): Indicates whether the sequentium is periodic.
        ground_truth (List[int]): The expected elements of the sequentium.
        ground_truth_length (int): The expected length of the sequentium.
    """

    sequence: Type[Sequence] = None
    sequence_name: str = None
    is_finite: bool = False
    is_periodic: bool = False
    ground_truth: List[int] = None
    ground_truth_length: int = None

    def test_sequence_name(self):
        """Test if the sequentium's name matches the expected value."""
        if self.sequence.__str__() != self.sequence_name:
            raise ValueError(f'Expected: {self.sequence_name}. Got {self.sequence.__str__()}')

    def test_is_finite(self):
        """Test if the sequentium's finiteness matches the expected value."""
        if self.sequence.is_finite != self.is_finite:
            raise ValueError

    def test_is_periodic(self):
        """Test if the sequentium's periodicity matches the expected value."""
        if self.sequence.is_periodic != self.is_periodic:
            raise ValueError

    def test_len(self):
        """Test the length of the sequentium, considering finiteness."""
        if self.sequence.is_finite:
            assert len(self.sequence) == self.ground_truth_length
        else:
            with pytest.raises(InfiniteSequenceError):
                len(self.sequence)

    def test_getitem(self):
        """Test if sequentium elements match the expected ground truth."""
        error_msg = ''
        for index, element in enumerate(self.ground_truth):
            if self.sequence[index] != element:
                error_msg += f'{index}. Expected: {element} at index {index}, but got {self.sequence[index]}.\n'

        if error_msg:
            raise ValueError(error_msg)

    def test_contains(self):
        """Test if elements from the ground truth are correctly identified in the sequentium."""
        error_msg = ''
        for index, element in enumerate(self.ground_truth):
            if (element in self.sequence) is False:
                error_msg += f'{index}. The expression ({element} in sequentium) must be True, but it is not.'

        if error_msg:
            raise ValueError(error_msg)

    def test_not_contains(self):
        """Test if elements not in the ground truth are correctly identified as not in the sequentium."""
        error_msg = ''
        count = 0
        for element in range(len(self.ground_truth)):
            if element not in self.ground_truth and (element not in self.sequence) is False:
                error_msg += f'{count}. The expression ({element} in sequentium) must be False, but it is not. \n'
                count += 1
        if error_msg:
            raise ValueError(error_msg)

    def test_as_list(self):
        """Test if the as_list method returns the expected subsequence for various start and stop indices."""
        error_msg = ''
        count = 0
        for j in range(self.ground_truth_length - 1):
            for i in range(j, self.ground_truth_length):
                if self.sequence[j:i] != self.ground_truth[j:i]:
                    error_msg += f"{count}. Expected: {self.ground_truth[j:i]}. " \
                                 f"Got {self.sequence[j:i]}!\n" \
                                 f" -> parameters: start = {j}, stop = {i}.\n"
                    count += 1
        if error_msg:
            raise Exception(error_msg)


class FiniteSequenceTestSuite(SequenceTestSuite):
    """Test suite for evaluating properties and behavior of finite sequences."""

    is_finite = True


class PeriodicSequenceTestSuite(SequenceTestSuite):
    """
    Test suite for evaluating properties and behavior of periodic sequences.

    Attributes:
        period_length (int): The expected period length of the sequentium.
    """

    is_periodic = True
    period_length: int

    def test_is_periodic(self):
        """Test if the sequentium's periodicity matches the expected value."""
        if self.sequence.is_periodic != self.is_periodic:
            raise ValueError(f'Expected a periodic sequentium, but got {self.sequence.is_periodic}.')

    def test_period(self):
        """Test if the sequentium's period matches the expected period length."""
        if self.period_length != self.sequence.period:
            raise ValueError(f'Expected period: {self.period_length}, but got {self.sequence.period}.')
