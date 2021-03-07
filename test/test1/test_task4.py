"""TEST Homework 1.4.

Check how many zero tuples.
"""
import pytest

from hw.hw1.task4 import check_sum_of_four


@pytest.mark.parametrize(
    ("a", "b", "c", "d", "expected_result"),
    [
        ([0, 0], [0, 0], [0, 0], [0, 0], 16),
        ([1, 1], [1, 1], [1, 1], [1, 1], 0),
        ([0, 1], [0, 0], [0, 0], [0, 0], 8),
        ([1, 2], [-1, 0], [3, 7], [-3, -7], 2),
        ([], [], [], [], 0),
        (
            [-3, 4, 54, 23, -15, 63, -76, 13, 122, -4, 2, 6],
            [-3, 4, 54, 23, -15, 63, -76, 13, 122, -4, 2, 6],
            [-3, 4, 54, 23, -15, 63, -76, 13, 122, -4, 2, 6],
            [-3, 4, 54, 23, -15, 63, -76, 13, 122, -4, 2, 6],
            66,
        ),
    ],
)
def test_check_sum_of_four(a: list, b: list, c: list, d: list, expected_result: bool):
    actual_result = check_sum_of_four(a, b, c, d)

    assert actual_result == expected_result
