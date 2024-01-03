from abc import ABC, abstractmethod
from itertools import islice
from typing import Any, Generator, Union, List, Optional

from sequence.core.utils.exceptions import NotPeriodicSequenceError


class SequenceMixin(ABC):

    @abstractmethod
    def __contains__(self, item: Any) -> bool:
        raise NotImplementedError

    @abstractmethod
    def __len__(self) -> int:
        raise NotImplementedError

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
    def _as_list(self, stop: int, start: Optional[int] = None, step: Optional[int] = None) -> List[Any]:
        """Return a list representation of the sequence within the specified range (internal use)."""
        raise NotImplementedError

    @abstractmethod
    def _at(self, index: int) -> Any:
        """Get the element at the specified index in the sequence (internal use)."""
        raise NotImplementedError
