"""Homework 3.1.

Write parametrize decorator that caches function data.
"""
from collections import Callable


def cache(times: int) -> Callable:
    """Give to cache decorator parameter times.

    Args:
        times: number of time the return from the same arg will be repeated.

    Returns: wrapper

    """

    def our_decorator(func: Callable) -> Callable:
        """Cache the data in func, so if args are the same it doesnot count, but return previously counted data.

        Args:
            func: function to be modified

        Returns: function with modification

        """
        old_data = {}

        count = 0

        def wrapper(*arg: (int, str)) -> (int, str):
            if arg in old_data and old_data[arg][1] < times:
                old_data[arg][1] += 1
                return old_data[arg][0]

            old_data[arg] = [func(*arg), count]
            return old_data[arg][0]

        return wrapper

    return our_decorator
