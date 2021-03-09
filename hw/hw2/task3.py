"""Homework 2.3.

Gives combinations of elements from different lists.
"""
from itertools import product
from typing import Any, List


def combinations(*args: List[Any]) -> List[List]:
    """Give combination of input arrays without crossing.

    Args:
        *args: list of elements

    Returns: list of combination lists

    """
    return [list(i) for i in product(*args)]
