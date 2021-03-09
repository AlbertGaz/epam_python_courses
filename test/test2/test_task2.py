"""TEST Homework 2.1.

Check correctness of function parsing text file.
"""
import pytest

from hw.hw2.task2 import major_and_minor_elem


@pytest.mark.parametrize(
    ("inp", "expected_result"),
    [
        ([1, 2, 1], (1, 2)),
        (
            [
                1,
                2,
                3,
                4,
                5,
                6,
                7,
                8,
                9,
                "a",
                "a",
                "a",
                "a",
                "a",
                "a",
                "a",
                "a",
            ],
            ("a", 1),
        ),
    ],
)
def test_major_and_minor_elem(inp: str, expected_result: list):
    actual_result = major_and_minor_elem(inp)

    assert actual_result == expected_result
