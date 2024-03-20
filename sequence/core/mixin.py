from typing import Any, List, ClassVar

from sequence.core.utils.functions import is_in_monotonic_increasing_generator


class MonotonicIncreasingMixin:
    """Mixin class for monotonic increasing sequences."""

    def __contains__(self, item: Any) -> bool:
        return is_in_monotonic_increasing_generator(generator=self, item=item)


class AlmostMonotonicIncreasingMixin:
    """Mixin class for almost monotonic increasing sequences."""

    offset: ClassVar[List[Any]]

    def __contains__(self, item: Any) -> bool:
        if item in self.offset:
            return True
        return is_in_monotonic_increasing_generator(generator=self[len(self.offset) :], item=item)
