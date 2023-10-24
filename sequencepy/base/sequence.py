from abc import ABC, abstractmethod
from itertools import islice
from typing import Generator, List, Tuple


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
    def _at(self, index: int) -> int:
        raise NotImplementedError


class FiniteSequence(Sequence):

    def __init__(self):
        super().__init__()
        self.sequence: List[int] = None

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
        return self.sequence[start:end:step]

    def _at(self, index: int) -> int:
        return self.sequence[index]


class InfiniteSequence(Sequence):

    @property
    def is_finite(self) -> bool:
        return False

    def __len__(self) -> int:
        raise ValueError

    def as_list(self, end: int, start: int = 0, step: int = 1) -> List[int]:
        return list(islice(self, start, end, step))

    def _at(self, index: int) -> int:
        return next(islice(self, index, index + 1))


class MonotonlyIncreasing(Sequence):

    def __contains__(self, item: int) -> bool:
        for element in self.as_generator():
            if element == item:
                return True
            if element > item:
                return False


class Explicit(InfiniteSequence):

    def __init__(self, start_index: int = 0):
        super().__init__()
        self.start_index = start_index

    def as_generator(self) -> Generator:
        index = self.start_index
        while True:
            yield self.formula(index=index)
            index += 1

    @abstractmethod
    def formula(self, index: int) -> int:
        raise NotImplementedError


class Recursive(InfiniteSequence):

    def __init__(self, start_terms: Tuple[int, ...] = None):
        super().__init__()
        self.start_terms = start_terms

    def as_generator(self) -> Generator:
        terms = self.start_terms
        while True:
            yield terms[0]
            terms = self.formula(terms=terms)

    @abstractmethod
    def formula(self, terms: Tuple[int, ...]) -> Tuple[int, ...]:
        raise NotImplementedError


class PropertyDefined(InfiniteSequence):

    def __contains__(self, item: int) -> bool:
        return self.property(number=item)

    def as_generator(self) -> Generator:
        number = 1
        while True:
            if self.property(number=number):
                yield number
            number += 1

    @abstractmethod
    def property(self, number: int) -> bool:
        raise NotImplementedError
