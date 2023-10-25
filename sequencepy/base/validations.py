from sequencepy.base.errors import NegativeNumberError


def _validate_positive_integer(integer: int) -> None:
    """ The method validates that an object is a positive integer """
    if isinstance(integer, int) is False:
        raise ValueError(f'Expected an int type, but got {type(integer).__name__} type!')
    if integer < 0:
        raise NegativeNumberError(f'Expected a non-negative integer but got {integer}!')


def _validate_as_list_input(start: int, end: int, step: int) -> None:
    """ The method validates the input of the as_list method """
    _validate_positive_integer(integer=start)
    _validate_positive_integer(integer=end)
    _validate_positive_integer(integer=step)

    if end < start:
        raise ValueError(f'Variable end (={end}) must be greater than variable start (={start}!')
    if step > end - start:
        raise ValueError(f'Variable step (={step}) is too big.')
