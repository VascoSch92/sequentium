from typing import Any

from sequence.core.infinite_type import Explicit
from sequence.core.mixin import MonotonicIncreasingMixin
from sequence.core.utils.validation import validate_positive_integer


class GeneralisedNexusNumbers(MonotonicIncreasingMixin, Explicit):
    """
    Class representing a sequence of Generalised Nexus Numbers (https://mathworld.wolfram.com/NexusNumber.html).

    Attributes:
        dimension (int): The dimension parameter for the Generalised Nexus Numbers.
    """
    sequence_name = 'generalised Nexus numbers'

    def __init__(self, dimension: int) -> None:
        super().__init__()
        self.dimension = validate_positive_integer(integer=dimension)

    def formula(self, index: int) -> int:
        return (index + 1) ** (self.dimension + 1) - index ** (self.dimension + 1)


class PolygonalNumbers(Explicit):
    """
        Represents a class for generating and working with polygonal numbers.

        Attributes:
        - number_of_sides (int): The number of sides for the polygonal numbers.
    """
    sequence_name = 'polygonal numbers'

    def __init__(self, number_of_sides: int) -> None:
        super().__init__()
        self.number_of_sides = validate_positive_integer(integer=number_of_sides)

    def __contains__(self, item: Any) -> bool:
        if item < 0:
            return False
        if item == 0:
            return True

        item = (
            (
                    8 * (self.number_of_sides - 2) * item + (self.number_of_sides - 4) ** 2
            ) ** (1/2)
            + (self.number_of_sides - 4)
        ) / (2 * (self.number_of_sides - 2))
        return item == int(item)

    def formula(self, index: int) -> int:
        return (self.number_of_sides - 2) * index * (index-1) // 2 + index
