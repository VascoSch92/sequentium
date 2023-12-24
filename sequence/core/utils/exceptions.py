class NegativeNumberError(ValueError):
    """Error raise when trying to use a negative integer instead of a positive one."""


class InfiniteSequenceError(Exception):
    """Error raised when asking for finite sequence property to an infinite sequence."""


class NotPeriodicSequenceError(Exception):
    """Error raised when asking period to a non-periodic sequence."""
