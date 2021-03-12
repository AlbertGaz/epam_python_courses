"""TEST Homework 3.1.

Write cache decorator with parameter times, that describe number of repetition.
"""
from hw.hw3.task1 import cache


@cache(3)
def func(a):
    return a ** 2


def test_cache():
    a = func(100)
    assert func(100) is a
    assert func(100) is a
    assert func(100) is a
    assert func(100) is not a
