"""TEST Homework 2.5.

Check correctness of custom_range.
"""
import pytest

from hw.hw2.task5 import custom_range


@pytest.mark.parametrize(
    ("iterat", "args", "expected_result"),
    [
        ([1, 2, 3, 4, 5], [1, 4], [1, 2, 3]),
        ("abcdefg", ["a", "d", 2], ["a", "c"]),
        ("abcdefg", ["d", "a", -2], ["d", "b"]),
    ],
)
def test_custom_range(iterat, args, expected_result):
    actual_result = custom_range(iterat, *args)

    assert actual_result == expected_result
