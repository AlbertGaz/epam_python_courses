"""Homework 7.2."""


def backspace_compare(first: str, second: str) -> bool:
    """Check similarity of two strings after backspace #.

    Args:
        first: first string
        second: second string

    Returns: bool

    """
    res = []
    for s in [first, second]:
        if not s:
            res.append(s)
            continue
        s = "".join([s[i] for i in range(len(s) - 1) if s[i + 1] != "#"]) + s[-1] * (
            s[-1] != "#"
        )
        s = s.replace("#", "")
        res.append(s)
    return res[0] == res[1]
