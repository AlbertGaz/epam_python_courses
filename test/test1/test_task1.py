"""TEST Homework 1.1.

Check correctness of check_power_of_2.
"""
import pytest

from hw.hw1.task1 import check_power_of_2


@pytest.mark.parametrize(
    ("value", "expected_result"),
    [(0, False), (1, True), (2, True), (8, True), (1024, True), (2 ** 100, True)],
)
def test_power_of_2(value: int, expected_result: bool):
    actual_result = check_power_of_2(value)

    assert actual_result == expected_result
