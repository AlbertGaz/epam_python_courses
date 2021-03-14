"""Homework 4.4.

FizzBuzz numbers.
"""
import doctest
from typing import List


def fizzbuzz(n: int) -> List[str]:
    r"""Get fizzbuzz numbers.

    Args:
        n: number up to get fizzbuzz numbers

    Returns: list of fizzbuzz up to n

    - Install Python 3.8 (https://www.python.org/downloads/)
    - Install pytest `pip install pytest`
    - Clone the repository <path your repository>
    - Checkout branch <your branch>
    - Open terminal
    - Navigate to where tour python file, is using the commands 'cd' (change directory).
    For our example
    > D:\EPAM\courses\epam_python_courses\hw\hw4
    - Import package doctest 'import doctest'
    - Run command python -m doctest 'your_file.py'

    >>> fizzbuzz(1)
    [1]

    >>> fizzbuzz(5)
    [1, 2, 'fizz', 4, 'buzz']

    >>> fizzbuzz(0)
    Traceback (most recent call last):
    ValueError: Input Error!

    >>> fizzbuzz(-100)
    Traceback (most recent call last):
    ValueError: Input Error!

    >>> fizzbuzz(1.1)
    Traceback (most recent call last):
    ValueError: Input Error!
    """
    if type(n) != int or n < 1:
        raise ValueError("Input Error!")
    return [
        "fizzbuzz"
        if i % 15 == 0
        else "fizz"
        if i % 3 == 0
        else "buzz"
        if i % 5 == 0
        else i
        for i in range(1, n + 1)
    ]


if __name__ == "__main__":
    doctest.testmod()
