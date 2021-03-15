"""Homework 4.5.

FizzBuzz numbers in FP.
"""
from typing import Generator


def fizzbuzz(n: int) -> Generator:
    """Generate fizzbuzz.

    Args:
        n: int

    Returns: generator

    """
    namenum = (
        lambda x: (x % 15 == 0 and "fizzbuzz")
        or (x % 3 == 0 and "fizz")
        or (x % 5 == 0 and "buzz")
        or x
    )
    for i in map(namenum, range(1, n + 1)):
        yield i
