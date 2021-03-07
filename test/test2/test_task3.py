"""TEST Homework 2.3.

Check correctness of function making combinations.
"""
import pytest

from hw.hw2.task3 import combinations


@pytest.mark.parametrize(
    ("args", "expected_result"),
    [
        ([[1], [2, 3]], [[1, 2], [1, 3]]),
        (
            [[1, 2, 3], [4, 5, 6]],
            [[1, 4], [1, 5], [1, 6], [2, 4], [2, 5], [2, 6], [3, 4], [3, 5], [3, 6]],
        ),
    ],
)
def test_combinations(args: list, expected_result: list):
    actual_result = combinations(*args)

    assert actual_result == expected_result
