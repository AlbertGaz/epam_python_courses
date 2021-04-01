"""TEST Homework 7.3."""
from typing import List

import pytest

from hw.hw7.hw7_task3 import tic_tac_toe_checker


@pytest.mark.parametrize(
    ("value", "expected_result"),
    [
        ([["x", "x", "x"], ["-", "-", "-"], ["-", "-", "-"]], "x wins!"),
        ([["x", "-", "-"], ["x", "-", "-"], ["x", "-", "-"]], "x wins!"),
        ([["x", "-", "x"], ["-", "x", "-"], ["-", "-", "x"]], "x wins!"),
        ([["x", "x", "x"], ["o", "o", "o"], ["-", "-", "-"]], "draw!"),
        ([["x", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]], "unfinished!"),
        ([["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]], "draw!"),
    ],
)
def test_tic_tac_toe_checker(value: List[List[str]], expected_result: str):
    actual_result = tic_tac_toe_checker(value)

    assert actual_result == expected_result
