from abc import ABC, abstractmethod, abstractclassmethod
from itertools import islice
from typing import Generator, List, Tuple, Union


class Sequence(ABC):

    def __init__(self):
        self.formula_type: str = ''

        self.start_terms: Tuple[int] = tuple()

    def __len__(self):
        raise ValueError('The sequence contains an infinite number of elements')

    @abstractmethod
    def __contains__(self, item):
        raise NotImplementedError

    def __iter__(self, item):
        return self.generator()

    def __getitem__(self, item):
        return self.get_element(index=item)

    def generator(self, start: int = 0) -> Generator:
        if self.formula_type == 'explicit':
            return self._generator_explicit_sequence(start=start)
        elif self.formula_type == 'recursive':
            return self._generator_recursive_sequence()
        elif self.formula_type == 'partial_sum':
            raise NotImplementedError
        else:
            raise NotImplementedError

    def _generator_explicit_sequence(self, start: int = 0) -> Generator:
        index = start
        while True:
            yield self.formula(index=index)
            index += 1

    def _generator_recursive_sequence(self) -> Generator:
        terms = self.start_terms
        while True:
            yield terms[0]
            terms = self.formula(terms=terms)

    def _generator_partial_sum_sequence(self) -> Generator:
        index = 0
        partial_sum = 0
        while True:
            yield partial_sum
            partial_sum += self.formula(index=index)

    @abstractmethod
    def formula(self, **kwargs) -> Union[Tuple, int]:
        raise NotImplementedError

    def list(self, end: int, start: int = 0) -> List[int]:
        # FIXME: decide how we want to start
        return list(islice(self.generator(), start, end))

    def get_element(self, index: int) -> int:
        return next(islice(self.generator(), index, index + 1))
