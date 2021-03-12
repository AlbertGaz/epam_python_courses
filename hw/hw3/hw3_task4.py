"""Homework 3.4.

Define armstrong number
"""


def is_armstrong(number: int) -> bool:
    """Define armstrong nuber.

    Args:
        number: int

    Returns: bool. True - number is armstrong.

    """
    return number == sum(
        map(lambda x: x ** len(str(number)), (int(digit) for digit in str(number)))
    )
