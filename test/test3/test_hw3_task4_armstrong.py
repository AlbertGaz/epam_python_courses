"""TEST Homework 3.4.

Define armstrong.
"""
import pytest

from hw.hw3.task4 import is_armstrong


@pytest.mark.parametrize(
    ("value", "expected_result"), [(153, True), (9, True), (11, False)]
)
def test_is_armstrong(value, expected_result):
    actual_result = is_armstrong(value)
    assert actual_result == expected_result
