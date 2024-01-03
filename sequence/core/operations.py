from abc import ABC, abstractmethod
from dataclasses import dataclass
from itertools import islice
from typing import Generator, Any, Union, List, Optional

from sequence.core.utils.validation import validate_as_list_input
from sequence.core.core_mixin import SequenceMixin


class OperationMixin:

    def _as_list(self, stop: int, start: Optional[int] = None, step: Optional[int] = None) -> List[int]:
        stop, start, step = validate_as_list_input(start=start, stop=stop, step=step)
        return list(islice(self, start, stop, step))

    def _at(self, index: int) -> int:
        return next(islice(self, index, index + 1))


@dataclass(frozen=True)
class AddSequences(OperationMixin, SequenceMixin):
    sequence_a: Any
    sequence_b: Any

    def __add__(self, other):
        return AddSequences(self, other)

    def __contains__(self, item):
        return True

    def __len__(self) -> int:
        if self.sequence_a.is_finite and self.sequence_b.is_finite:
            return len(self.sequence_a) + len(self.sequence_b)
        raise Exception

    @property
    def is_finite(self) -> bool:
        if self.sequence_a.is_finite and self.sequence_b.is_finite:
            return True
        return False

    @property
    def is_periodic(self) -> bool:
        if self.sequence_a.is_periodic and self.sequence_b.is_periodic:
            return True
        return False

    @property
    def period(self) -> int:
        # https://cs.stackexchange.com/questions/117397/period-of-sum-of-two-periodic-sequences
        return 0

    def _as_generator(self) -> Generator:
        for item1, item2 in zip(self.sequence_a, self.sequence_b):
            yield item1 + item2


@dataclass()
class AddSequenceAndConstant:
    sequence: Any
    constant: Union[float, int]

    def __add__(self, other):
        return AddSequenceAndConstant(sequence=self.sequence, constant=self.constant)

    def __post_init__(self):
        if self.constant == 0:
            return self.sequence
        return AddSequences(sequence_a= self.sequence, sequence_b=self.constant_generator())

    def constant_generator(self) -> Generator:
        while True:
            yield self.constant



