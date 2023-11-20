from typing import List, Type

import pytest

from sequence.core.core import Sequence


class SequenceTestSuite:
    sequence: Type[Sequence] = NotImplementedError
    is_finite: bool = False
    ground_truth: List[int] = NotImplementedError
    ground_truth_length: int = NotImplementedError

    def test_is_finite(self):
        if self.sequence.is_finite != self.is_finite:
            raise ValueError

    def test_len(self):
        if self.sequence.is_finite:
            assert len(self.sequence) == self.ground_truth_length
        else:
            with pytest.raises(ValueError):
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
                if self.sequence.as_list(start=j, end=i) != self.ground_truth[j:i]:
                    raise Exception


class FiniteSequenceTestSuite(SequenceTestSuite):
    is_finite = True
