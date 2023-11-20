from abc import ABC, abstractmethod
from itertools import islice
from typing import Generator, List, Tuple, Any

from sequence.core.validations import validate_positive_integer, _validate_as_list_input
from sequence.core.errors import InfiniteSequenceError


class Sequence(ABC):

    @abstractmethod
    def __contains__(self, item):
        raise NotImplementedError

    def __iter__(self):
        return self.as_generator()

    def __getitem__(self, item):
        return self._at(index=item)

    @abstractmethod
    def is_finite(self) -> bool:
        raise NotImplementedError

    @abstractmethod
    def as_generator(self) -> Generator:
        raise NotImplementedError

    @abstractmethod
    def as_list(self, end: int, start: int = 0, step: int = 1) -> List[int]:
        raise NotImplementedError

    @abstractmethod
    def _at(self, index: int) -> Any:
        raise NotImplementedError


class FiniteSequence(Sequence):

    def __init__(self):
        super().__init__()
        self.sequence: List[Any] = None

    def __contains__(self, item: int) -> bool:
        return item in self.sequence

    def __len__(self) -> int:
        return len(self.sequence)

    @property
    def is_finite(self) -> bool:
        return True

    def as_generator(self) -> Generator:
        for element in self.sequence:
            yield element

    def as_list(self, end: int, start: int = 0, step: int = 1) -> List[int]:
        _validate_as_list_input(start=start, end=end, step=step)
        return self.sequence[start:end:step]

    def _at(self, index: int) -> Any:
        return self.sequence[index]


class InfiniteSequence(Sequence):

    @property
    def is_finite(self) -> bool:
        return False

    def __len__(self) -> int:
        raise InfiniteSequenceError

    def as_list(self, end: int, start: int = 0, step: int = 1) -> List[int]:
        _validate_as_list_input(start=start, end=end, step=step)
        return list(islice(self, start, end, step))

    def _at(self, index: int) -> int:
        validate_positive_integer(integer=index)
        return next(islice(self, index, index + 1))

