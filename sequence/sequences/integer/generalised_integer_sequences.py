from sequence.core.infinite_type import Explicit, MonotonicIncreasing


class GeneralisedNexusNumbers(MonotonicIncreasing, Explicit):

    def __init__(self, dimension: int = None):
        super().__init__()
        self.dimension = dimension

    def formula(self, index: int) -> int:
        return (index + 1) ** (self.dimension + 1) - index ** (self.dimension + 1)
