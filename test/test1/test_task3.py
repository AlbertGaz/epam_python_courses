"""TEST Homework 1.3.

Check if we get min max from file.
"""
import pytest

from hw.hw1.task3 import find_maximum_and_minimum


@pytest.mark.parametrize(
    ("value", "expected_result"),
    [
        ("test/test1/test_samples_task3/test_sample_task3_1.txt", (1, 5)),
        ("test/test1/test_samples_task3/test_sample_task3_2.txt", (-1203, 3223)),
        ("test/test1/test_samples_task3/test_sample_task3_3.txt", (5, 5)),
    ],
)
def test_min_max(value: str, expected_result: bool):
    actual_result = find_maximum_and_minimum(value)

    assert actual_result == expected_result
