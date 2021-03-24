"""Homework 5.2."""
import functools
from typing import Callable


def wraps(func: Callable) -> Callable:
    """Decorate function to save doc and name from original function.

    Args:
        func: function to save doc and name

    Returns: wrapper
    """

    def update_atr(wrapper: Callable, func: Callable) -> Callable:
        wrapper.__name__ = func.__name__
        wrapper.__doc__ = func.__doc__
        wrapper.__original_func = func
        return wrapper

    return functools.partial(update_atr, func=func)
