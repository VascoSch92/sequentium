from abc import ABC, abstractmethod
from itertools import islice
from typing import Generator, List, Any

from sequence.core.utils.exceptions import InfiniteSequenceError, NotPeriodicSequenceError
from sequence.core.utils.validation import validate_positive_integer, validate_as_list_input


class Sequence(ABC):
    """Abstract base class for representing mathematical sequences."""

    @abstractmethod
    def __contains__(self, item):
        raise NotImplementedError

    def __iter__(self):
        return self.as_generator()

    def __getitem__(self, item):
        return self._at(index=item)

    @abstractmethod
    def is_finite(self) -> bool:
        """Check if the sequence is finite."""
        raise NotImplementedError

    @property
    def is_periodic(self) -> bool:
        """Check if the sequence is periodic."""
        return False

    @property
    def period(self) -> int:
        """Get the period of the sequence. Raises NotPeriodicSequenceError if the sequence is not periodic."""
        raise NotPeriodicSequenceError

    @abstractmethod
    def as_generator(self) -> Generator:
        """Return a generator for the sequence."""
        raise NotImplementedError

    @abstractmethod
    def as_list(self, stop: int, start: int = 0, step: int = 1) -> List[int]:
        """Return a list representation of the sequence within the specified range."""
        raise NotImplementedError

    @abstractmethod
    def _at(self, index: int) -> Any:
        """Get the element at the specified index in the sequence (internal use)."""
        raise NotImplementedError


class FiniteType(Sequence, ABC):
    """Abstract base class for representing finite sequences."""

    def __init__(self):
        super().__init__()
        self.sequence: List[Any] = None

    def __contains__(self, item: int) -> bool:
        return item in self.sequence


class InfiniteType(Sequence, ABC):
    """Abstract base class for representing infinite sequences."""

    @property
    def is_finite(self) -> bool:
        return False

    def __len__(self) -> int:
        raise InfiniteSequenceError

    def as_list(self, stop: int, start: int = 0, step: int = 1) -> List[int]:
        validate_as_list_input(start=start, stop=stop, step=step)
        return list(islice(self, start, stop, step))

    def _at(self, index: int) -> int:
        validate_positive_integer(integer=index)
        return next(islice(self, index, index + 1))
