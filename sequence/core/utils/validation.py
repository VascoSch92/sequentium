from sequence.core.utils.excpetions import NegativeNumberError
from typing import Tuple


def validate_integer(integer: int) -> None:
    """ The method validates that an object is an integer """
    if isinstance(integer, int) is False:
        raise ValueError(f'Expected an int type, but got {type(integer).__name__} type!')


def validate_positive_integer(integer: int) -> None:
    """ The method validates that an object is a positive integer """
    validate_integer(integer=integer)

    if integer < 0:
        raise NegativeNumberError(f'Expected a non-negative integer but got {integer}!')


def validate_integer_tuple(tuple: Tuple[int, ...], length: int) -> None:
    """ The method validates that an object is a tuple of integers """
    if isinstance(tuple, Tuple) is False:
        raise ValueError(f'Expected a tuple type, but got {type(tuple).__name__} type!')
    if len(tuple) != length:
        raise ValueError(f'They are needed exactly {length} terms. Got {len(tuple)}')
    for number in tuple:
        validate_positive_integer(integer=number)


def validate_as_list_input(start: int, stop: int, step: int) -> None:
    """ The method validates the input of the as_list method """
    validate_positive_integer(integer=start)
    validate_positive_integer(integer=stop)
    validate_positive_integer(integer=step)

