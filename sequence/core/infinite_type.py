from abc import abstractmethod, ABC
from typing import Generator, Any, Tuple, List

from sequence.core.core import InfiniteType
from sequence.core.utils.validation import validate_positive_integer, validate_as_list_input


class Explicit(InfiniteType, ABC):
    """Abstract base class for representing explicit infinite sequences."""

    def __init__(self, start_index: int = 0):
        super().__init__()
        validate_positive_integer(integer=start_index)
        self.start_index = start_index

    def _as_generator(self) -> Generator:
        index = self.start_index
        while True:
            yield self.formula(index=index)
            index += 1

    @abstractmethod
    def formula(self, index: int) -> Any:
        """Abstract method to define the formula for generating elements in the sequence."""
        raise NotImplementedError

    def _as_list(self, stop: int, start: int = None, step: int = None) -> List[int]:
        stop, start, step = validate_as_list_input(start=start, stop=stop, step=step)
        return [self.formula(index=index) for index in range(start, stop, step)]

    def _at(self, index: int) -> int:
        validate_positive_integer(integer=index)
        return self.formula(index=index)


class Recursive(InfiniteType, ABC):
    """Abstract base class for representing recursive infinite sequences."""

    def __init__(self, start_terms: Tuple[Any, ...] = None):
        super().__init__()
        self.start_terms = start_terms

    def _as_generator(self) -> Generator:
        terms = self.start_terms
        while True:
            yield terms[0]
            terms = self.formula(terms=terms)

    @abstractmethod
    def formula(self, terms: Tuple[Any, ...]) -> Tuple[Any, ...]:
        """Abstract method to define the recurrence relation of the sequence."""
        raise NotImplementedError


class PropertyDefined(InfiniteType, ABC):
    """Abstract base class for representing infinite sequences defined by a property."""

    def __contains__(self, item: Any) -> bool:
        return self.property(number=item)

    def _as_generator(self) -> Generator:
        number = 1
        while True:
            if self.property(number=number):
                yield number
            number += 1

    @abstractmethod
    def property(self, number: Any) -> bool:
        """Abstract method to define the property for elements in the sequence."""
        raise NotImplementedError


class MonotonicIncreasing:
    """Mixin class for monotonic increasing sequences."""

    def __contains__(self, item: Any) -> bool:
        for element in self._as_generator():
            if element == item:
                return True
            if element > item:
                return False
