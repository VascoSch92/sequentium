from sequence.core.utils.exceptions import NegativeNumberError
from typing import Tuple


def validate_integer(integer: int) -> int:
    """The method validates that an object is an integer."""
    if isinstance(integer, int) is False:
        raise ValueError(f'Expected an int type, but got {type(integer).__name__} type!')
    else:
        return integer


def validate_positive_integer(integer: int) -> int:
    """The method validates that an object is a positive integer."""
    if validate_integer(integer=integer) < 0:
        raise NegativeNumberError(f'Expected a non-negative integer but got {integer}!')
    else:
        return integer


def validate_integer_tuple(tuple: Tuple[int, ...], length: int) -> None:
    """ The method validates that an object is a tuple of integers """
    if isinstance(tuple, Tuple) is False:
        raise ValueError(f'Expected a tuple type, but got {type(tuple).__name__} type!')
    if len(tuple) != length:
        raise ValueError(f'They are needed exactly {length} terms. Got {len(tuple)}')
    for number in tuple:
        validate_positive_integer(integer=number)


def validate_as_list_input(start: int, stop: int, step: int) -> Tuple[int, int, int]:
    """ The method validates the input of the as_list method """
    start = 0 if start is None else start
    step = 1 if step is None else step
    return stop, start, step

