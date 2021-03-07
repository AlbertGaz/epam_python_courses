"""TEST Homework 1.2.

Check if int sequence is fibonacci.
"""
import pytest

from hw.hw1.task2 import check_fibonacci


@pytest.mark.parametrize(
    ("sequence", "expected_result"),
    [
        ([], False),
        ([0], True),
        ([13], True),
        ([-1, 0], False),
        ([0, 1], True),
        ([5, 8, 13], True),
        ([1, 1], True),
        ([1, 1, 1], False),
        ([354224848179261915075, 573147844013817084101, 927372692193078999176], True),
    ],
)
def test_fib_seq(sequence: list, expected_result: bool):
    actual_result = check_fibonacci(sequence)

    assert actual_result == expected_result
