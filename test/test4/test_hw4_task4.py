"""TEST Homework 4.4."""
import pytest

from hw.hw4.hw4_task4 import fizzbuzz


@pytest.mark.parametrize(
    ("n", "expected"),
    [(1, [1]), (10, [1, 2, "fizz", 4, "buzz", "fizz", 7, 8, "fizz", "buzz"])],
)
def test_fuzzbuzz_good_input(n, expected):
    actual_result = fizzbuzz(n)
    assert actual_result == expected


@pytest.mark.parametrize(("n"), [(-1), (0), (1.1)])
def test_fuzzbuzz_bad_input(n):
    with pytest.raises(ValueError, match="Input Error!"):
        fizzbuzz(n)
