"""TEST Homework 1.5.

Check maximum sub-array.
"""
import pytest

from hw.hw1.task5 import find_maximal_subarray_sum


@pytest.mark.parametrize(
    ("nums", "k", "expected_result"),
    [
        ([1, 3, -1, -3, 5, 3, 6, 7], 3, 16),
        ([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 10, 10),
        ([-100, -1000, 1, -10, -1], 4, 1),
    ],
)
def test_find_maximal_subarray_sum(nums: list, k: int, expected_result: int):
    actual_result = find_maximal_subarray_sum(nums, k)

    assert actual_result == expected_result
