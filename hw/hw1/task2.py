"""Homework 1.2.

Check sequence for Fibonacciness.
"""
from typing import Sequence


def fib_gen() -> int:
    """Fibonacci generator.

    Returns: elements of fibonacci sequence
    """
    yield 0
    yield 1
    s1 = 0
    s2 = 1
    while True:
        s = s1 + s2
        s1, s2 = s2, s
        yield s


def check_fibonacci(data: Sequence[int]) -> bool:
    """Check if sequence is fib.

    Args:
        data: sequence to be checked on fibonacciness
    Returns: True - sequence is from fibonacci, else no.
    """
    fgen = fib_gen()
    fib = -float("inf")
    if len(data) == 0:
        return False
    while fib < data[0]:
        fib = next(fgen)
    if fib != data[0]:
        return False
    for i in range(1, len(data)):
        if next(fgen) != data[i]:
            return False
    return True
