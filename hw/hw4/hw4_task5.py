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

    def name_num(x: int) -> (int, str):
        return "fizz" * (x % 3 == 0) + "buzz" * (x % 5 == 0) or x

    for i in map(name_num, range(1, n + 1)):
        yield i
