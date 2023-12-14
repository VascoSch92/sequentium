from sequence.core.infinite_type import Explicit, MonotonicIncreasing
from sequence.core.utils.validation import validate_positive_integer


class GeneralisedNexusNumbers(MonotonicIncreasing, Explicit):
    """
    Class representing a sequence of Generalised Nexus Numbers (https://mathworld.wolfram.com/NexusNumber.html).

    Attributes:
        dimension (int): The dimension parameter for the Generalised Nexus Numbers.
    """

    def __init__(self, dimension: int):
        super().__init__()
        self.dimension = validate_positive_integer(integer=dimension)

    def __str__(self):
        return 'generalised Nexus numbers'

    def formula(self, index: int) -> int:
        return (index + 1) ** (self.dimension + 1) - index ** (self.dimension + 1)
