from typing import List, Type

import pytest

from sequence.core.core import Sequence
from sequence.core.utils.errors import InfiniteSequenceError


class SequenceTestSuite:
    sequence: Type[Sequence] = None
    is_finite: bool = False
    is_periodic: bool = False
    ground_truth: List[int] = None
    ground_truth_length: int = None

    def test_is_finite(self):
        if self.sequence.is_finite != self.is_finite:
            raise ValueError

    def test_is_periodic(self):
        if self.sequence.is_periodic != self.is_periodic:
            raise ValueError

    def test_len(self):
        if self.sequence.is_finite:
            assert len(self.sequence) == self.ground_truth_length
        else:
            with pytest.raises(InfiniteSequenceError):
                len(self.sequence)

    def test_getitem(self):
        for index, element in enumerate(self.ground_truth):
            if self.sequence[index] != element:
                raise ValueError(f'Expected element: {element} at index {index}, but got {self.sequence[index]}!')

    def test_contains(self):
        for element in self.ground_truth:
            if (element in self.sequence) is False:
                raise ValueError(f'The expression ({element} in sequence) must be True, but it is not!')

    def test_not_contains(self):
        for element in range(len(self.ground_truth)):
            if element not in self.ground_truth and (element not in self.sequence) is False:
                raise ValueError(f'The expression ({element} in sequence) must be True, but it is not!')

    def test_as_list(self):
        for j in range(self.ground_truth_length - 1):
            for i in range(j, self.ground_truth_length):
                if self.sequence.as_list(start=j, stop=i) != self.ground_truth[j:i]:
                    raise Exception(
                        f'Expected: {self.ground_truth[j:i]}. Got {self.sequence.as_list(start=j, stop=i)}!'
                    )


class FiniteSequenceTestSuite(SequenceTestSuite):
    is_finite = True


class PeriodicSequenceTestSuite(SequenceTestSuite):
    is_periodic = True
    period_length: int

    def test_is_periodic(self):
        if self.sequence.is_periodic != self.is_periodic:
            raise ValueError

    def test_period(self):
        if self.period_length != self.sequence.period:
            raise ValueError(f'Expected period: {self.period_length}, but got {self.sequence.period}!')
