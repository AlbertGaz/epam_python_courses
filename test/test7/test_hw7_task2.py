"""TEST Homework 7.2."""
import pytest

from hw.hw7.hw7_task2 import backspace_compare


@pytest.mark.parametrize(
    ("first", "second", "expected_result"),
    [
        ("ab#c", "ad#c", True),
        ("a##c", "#a#c", True),
        ("#a#b#c#d#c", "####c", True),
        ("a##", "###", True),
        ("", "", True),
        ("albert", "gazaryan", False),
    ],
)
def test_backspace_recursion_variant(first: str, second: str, expected_result: bool):
    actual_result = backspace_compare(first, second)

    assert actual_result == expected_result
