class NegativeNumberError(ValueError):
    pass


class InfiniteSequenceError(Exception):
    """ Error raised when asking for finite sequence property to an infinite sequence. """


class NotPeriodicSequenceError(Exception):
    """ Error raised when asking period to a non-periodic sequence. """
