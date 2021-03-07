"""TEST Homework 2.4.

Check correctness of cache function.
"""
import pytest

from hw.hw2.task4 import cache


@cache
def func(a, b):
    return (a ** b) ** 2


@pytest.mark.parametrize(
    ("arg", "expected_result"),
    [
        ((1, 2), True),
    ],
)
def test_cache(arg, expected_result: list):
    actual_result = func(*arg) is func(*arg)
    assert actual_result == expected_result
