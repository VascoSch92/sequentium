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

    @abstractmethod
    def __str__(self):
        raise NotImplementedError

    def __iter__(self):
        return self._as_generator()

    def __getitem__(self, item):
        if isinstance(item, slice):
            if item.stop is None and self.is_finite is False:
                return InfiniteSequenceError
            return self._as_list(start=item.start, stop=item.stop, step=item.step)
        else:
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
    def _as_generator(self) -> Generator:
        """Return a generator for the sequence (internal use)."""
        raise NotImplementedError

    @abstractmethod
    def _as_list(self, stop: int, start: int = None, step: int = None) -> List[int]:
        """Return a list representation of the sequence within the specified range (internal use)."""
        raise NotImplementedError

    @abstractmethod
    def _at(self, index: int) -> Any:
        """Get the element at the specified index in the sequence (internal use)."""
        raise NotImplementedError


class FiniteType(Sequence, ABC):
    """Abstract base class for representing finite sequences."""

    def __init__(self, sequence: List[Any] = None):
        super().__init__()
        self.sequence = sequence

    def __contains__(self, item: int) -> bool:
        return item in self.sequence


class InfiniteType(Sequence, ABC):
    """Abstract base class for representing infinite sequences."""

    @property
    def is_finite(self) -> bool:
        return False

    def __len__(self) -> int:
        raise InfiniteSequenceError

    def _as_list(self, stop: int, start: int = None, step: int = None) -> List[int]:
        stop, start, step = validate_as_list_input(start=start, stop=stop, step=step)
        return list(islice(self, start, stop, step))

    def _at(self, index: int) -> int:
        return next(islice(self, index, index + 1))
