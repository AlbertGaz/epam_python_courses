"""Homework 1.4.

Check how many zero tuples
"""
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
    l_list = len(a)
    ab = {}
    cd = {}
    for i in range(l_list):
        for j in range(l_list):
            ab[a[i] + b[j]] = ab.get(a[i] + b[j], 0) + 1
            cd[c[i] + d[j]] = cd.get(c[i] + d[j], 0) + 1

    l_ab = len(ab)
    l_cd = len(cd)

    for i in range(l_ab):
        for j in range(l_cd):
            if list(ab.keys())[i] + list(cd.keys())[j] == 0:
                n += ab[list(ab.keys())[i]] * cd[list(cd.keys())[j]]
    return n
