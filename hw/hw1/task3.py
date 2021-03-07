"""Homework 1.3.

Give min max of input
"""
import re
from typing import Tuple


def find_maximum_and_minimum(file_name: str) -> Tuple[int, int]:
    """Find min max from file.

    Args:
        file_name: str

    Returns: tuple

    """
    with open(file_name) as f:
        patt = r"-?\d+"
        maxnum = -float("inf")
        minnum = float("inf")

        for line in f:
            num_line = re.findall(patt, line)
            int_line = [int(i) for i in num_line]
            if maxnum < max(int_line):
                maxnum = max(int_line)
            if minnum > min(int_line):
                minnum = min(int_line)
        return minnum, maxnum
