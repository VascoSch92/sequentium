class NegativeNumberError(ValueError):
    pass


class InfiniteSequenceError(Exception):
    """ Error raised when asking for finite sequentium property to an infinite sequentium. """


class NotPeriodicSequenceError(Exception):
    """ Error raised when asking period to a non-periodic sequentium. """
