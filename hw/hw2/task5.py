"""Homework 2.5.

Function that is custom range
"""


def custom_range(iterat: (list, str), *arg: (str, int)) -> list:
    """Give custom range.

    Args:
        iterat: input iterable object
        *arg: start, end and step

    Returns: list of objects iterated

    """
    if len(arg) == 3:
        start, end, step = arg
    elif len(arg) == 2:
        start, end, step = *arg, 1
    else:
        start, end, step = 0, arg, 1
    res = []
    for i in range(iterat.index(start), iterat.index(end), step):
        if i >= iterat.index(end) and step > 0 or i < iterat.index(end) and step < 0:
            return res
        res.append(iterat[i])

    return res
