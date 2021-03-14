"""Homework 4.4.

FizzBuzz numbers.
"""
from typing import List


def fizzbuzz(n: int) -> List[str]:
    """Get fizzbuzz numbers.

    Args:
        n: number up to get fizzbuzz numbers

    Returns: list of fizzbuzz up to n

    """
    return [
        "fizzbuzz"
        if i % 15 == 0
        else "fizz"
        if i % 3 == 0
        else "buzz"
        if i % 5 == 0
        else i
        for i in range(1, n + 1)
    ]
