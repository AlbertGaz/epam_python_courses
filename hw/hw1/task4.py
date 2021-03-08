"""Homework 1.4.

Check how many zero tuples
"""
from itertools import product
from typing import List


def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    """Check number of tuples.

    Args:
        a: list
        b: list
        c: list
        d: list

    Returns: number of possible zero tuples.
    """
    n = 0
    for i, j, k, m in product(a, b, c, d):
        if i + j + k + m == 0:
            n += 1
    return n
