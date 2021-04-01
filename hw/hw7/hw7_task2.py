"""Homework 7.2."""
import re


def backspace_compare(first: str, second: str) -> bool:
    """Check similarity of two strings after backspace #.

    Args:
        first: first string
        second: second string

    Returns: bool

    """
    if first == second:
        return True

    res = []
    patt = r".#"
    for s in [first, second]:
        s = re.sub(patt, "", s)
        s = s.replace("#", "")
        res.append(s)
    return res[0] == res[1]
