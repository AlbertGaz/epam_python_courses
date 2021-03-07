"""Homework1.1.

Check power of 2 of the input int.
"""


def check_power_of_2(a: int) -> bool:
    """Check if a is power of 2.

    Args:
        a: any int number
    Returns: bool. True - a is power of 2, False - not power of 2.
    """
    if (
        a == 1
    ):  # tricky number, because previous and next numbers (0 and 2) are powers of 2
        return False
    return not (bool(a & (a - 1)))
