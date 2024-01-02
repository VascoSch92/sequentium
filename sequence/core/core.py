from abc import ABC, abstractmethod
from itertools import islice
from typing import Generator, List, Any, Optional, Union

from sequence.core.utils.exceptions import InfiniteSequenceError, NotPeriodicSequenceError
from sequence.core.utils.validation import validate_as_list_input


class Sequence(ABC):
    """Abstract base class for representing mathematical sequences."""
    sequence_name: str

    @abstractmethod
    def __contains__(self, item: Any) -> bool:
        raise NotImplementedError

    def __eq__(self, other: Any) -> bool:
        """
        The method checks if the representation of the sequence is the same.
        It doesn't check that two sequences are equal, but that two sequences are different instance of the same class.
        """
        return other.__str__() == self.__str__() and other.__dict__ == self.__dict__

    def __str__(self) -> str:
        return self.sequence_name

    def __iter__(self) -> Generator:
        return self._as_generator()

    def __getitem__(self, item: Any) -> Union[List, Any]:
        if isinstance(item, slice):
            if item.stop is None and self.is_finite is False:
                return islice(self._as_generator(), item.start, None)
            return self._as_list(start=item.start, stop=item.stop, step=item.step)
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
    def _as_list(self, stop: int, start: Optional[int] = None, step: Optional[int] = None) -> List[int]:
        """Return a list representation of the sequence within the specified range (internal use)."""
        raise NotImplementedError

    @abstractmethod
    def _at(self, index: int) -> Any:
        """Get the element at the specified index in the sequence (internal use)."""
        raise NotImplementedError


class FiniteType(Sequence, ABC):
    """Abstract base class for representing finite sequences."""

    def __init__(self, sequence: Optional[List[Any]] = None) -> None:
        super().__init__()
        self.sequence = sequence

    def __contains__(self, item: Any) -> bool:
        return item in self.sequence


class InfiniteType(Sequence, ABC):
    """Abstract base class for representing infinite sequences."""

    @property
    def is_finite(self) -> bool:
        return False

    def __len__(self) -> int:
        raise InfiniteSequenceError

    def _as_list(self, stop: int, start: Optional[int] = None, step: Optional[int] = None) -> List[int]:
        stop, start, step = validate_as_list_input(start=start, stop=stop, step=step)
        return list(islice(self, start, stop, step))

    def _at(self, index: int) -> int:
        return next(islice(self, index, index + 1))
