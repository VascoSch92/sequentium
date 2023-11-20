from typing import List, Any

from sequence.core.core import FiniteType
from sequence.core.utils.validations import validate_as_list_input


class Finite(FiniteType):

    def __init__(self):
        super().__init__()

    def __len__(self) -> int:
        return len(self.sequence)

    @property
    def is_finite(self) -> bool:
        return True

    def as_list(self, stop: int, start: int = 0, step: int = 1) -> List[int]:
        validate_as_list_input(start=start, stop=stop, step=step)
        return self.sequence[start:stop:step]

    def _at(self, index: int) -> Any:
        return self.sequence[index]


class Periodic(FiniteType):

    @property
    def is_finite(self) -> bool:
        return False

    @property
    def is_periodic(self) -> bool:
        return True

    @property
    def period(self) -> int:
        raise NotImplementedError

    def as_list(self, stop: int, start: int = 0, step: int = 1) -> List[int]:
        raise NotImplementedError

    def _at(self, index: int) -> Any:
        raise NotImplementedError

