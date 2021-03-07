"""Homework 2.4.

Write a function that accepts another function as an argument. Then it
should return such a function, so the every call to initial one
should be cached.
"""
from collections import Callable


def cache(func: Callable) -> Callable:
    """Cache the data in func, so if args are the same it doesnot count, but return previously counted data.

    Args:
        func: function to be modified

    Returns: function with modification

    """
    old_data = {}

    def wrapper(*arg: (int, str)) -> (int, str):
        if arg in old_data:
            return old_data[arg]
        old_data[arg] = func(*arg)
        return old_data[arg]

    return wrapper
