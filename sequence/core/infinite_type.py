from abc import abstractmethod
from typing import Generator, Any, Tuple

from sequence.core.core import InfiniteSequence
from sequence.core.validations import validate_positive_integer


class Explicit(InfiniteSequence):

    def __init__(self, start_index: int = 0):
        super().__init__()
        validate_positive_integer(integer=start_index)
        self.start_index = start_index

    def as_generator(self) -> Generator:
        index = self.start_index
        while True:
            yield self.formula(index=index)
            index += 1

    @abstractmethod
    def formula(self, index: int) -> Any:
        raise NotImplementedError


class Recursive(InfiniteSequence):

    def __init__(self, start_terms: Tuple[Any, ...] = None):
        super().__init__()
        self.start_terms = start_terms

    def as_generator(self) -> Generator:
        terms = self.start_terms
        while True:
            yield terms[0]
            terms = self.formula(terms=terms)

    @abstractmethod
    def formula(self, terms: Tuple[Any, ...]) -> Tuple[Any, ...]:
        raise NotImplementedError


class PropertyDefined(InfiniteSequence):

    def __contains__(self, item: Any) -> bool:
        return self.property(number=item)

    def as_generator(self) -> Generator:
        number = 1
        while True:
            if self.property(number=number):
                yield number
            number += 1

    @abstractmethod
    def property(self, number: Any) -> bool:
        raise NotImplementedError


class MonotonicIncreasing:

    def __contains__(self, item: Any) -> bool:
        for element in self.as_generator():
            if element == item:
                return True
            if element > item:
                return False