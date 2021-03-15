"""TEST Homework 4.5."""
import pytest

from hw.hw4.hw4_task5 import fizzbuzz


@pytest.mark.parametrize(
    ("n", "expected"),
    [(1, [1]), (10, [1, 2, "fizz", 4, "buzz", "fizz", 7, 8, "fizz", "buzz"])],
)
def test_fizzbuzz(n, expected):
    actual_result = list(fizzbuzz(n))
    assert actual_result == expected
