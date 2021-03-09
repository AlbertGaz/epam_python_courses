"""Homework 2.2.

Find most common element.

Example 1:
Input: [3,2,3]
Output: 3, 2
Example 2:
Input: [2,2,1,1,1,2,2]
Output: 2, 1
"""
from typing import List, Tuple


def major_and_minor_elem(inp: List) -> Tuple[int, int]:
    """Find the most and least common elements.

    Args:
        inp: list of n elements

    Returns: tuple of size 2. first is most common element, second is least common element

    """
    min_el = sorted(set(inp), key=inp.count)[0]
    max_el = sorted(set(inp), key=inp.count)[-1]
    return max_el, min_el
