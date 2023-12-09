from abc import ABC
from typing import List, Any, Generator

from sequence.core.core import FiniteType
from sequence.core.utils.exceptions import InfiniteSequenceError
from sequence.core.utils.validation import validate_as_list_input


class Finite(FiniteType, ABC):
    """Abstract base class for representing finite sequences."""

    def __init__(self):
        super().__init__()

    def __len__(self) -> int:
        return len(self.sequence)

    @property
    def is_finite(self) -> bool:
        return True

    def _as_generator(self) -> Generator:
        for element in self.sequence:
            yield element

    def _as_list(self, stop: int, start: int = 0, step: int = 1) -> List[int]:
        stop, start, step = validate_as_list_input(start=start, stop=stop, step=step)
        return self.sequence[start:stop:step]

    def _at(self, index: int) -> Any:
        return self.sequence[index]


class Periodic(FiniteType, ABC):
    """Abstract base class for representing periodic sequences."""

    def __init__(self, _period: int):
        super().__init__()
        self._period = _period

    def __len__(self) -> int:
        raise InfiniteSequenceError

    @property
    def is_finite(self) -> bool:
        return False

    @property
    def is_periodic(self) -> bool:
        return True

    @property
    def period(self) -> int:
        return self._period

    def _as_generator(self) -> Generator:
        index = 0
        while True:
            yield self.sequence[index]
            index = (index + 1) % self._period

    def _as_list(self, stop: int, start: int = None, step: int = None) -> List[int]:
        stop, start, step = validate_as_list_input(start=start, stop=stop, step=step)
        return [self.sequence[index % self._period] for index in range(start, stop, step)]

    def _at(self, index: int) -> Any:
        return self.sequence[index % self._period]

