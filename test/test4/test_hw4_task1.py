"""TEST Homework 4.1.

Check function read_magic_number.
"""

import os

import pytest

from hw.hw4.hw4_task1 import read_magic_number


def file_maker(text):
    with open("test_hw4_task1_sample.txt", "w", encoding="utf-8") as f:
        f.write(str(text))
    return "test_hw4_task1_sample.txt"


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        (1, True),
        (2, True),
        (2.999999, True),
        (3, False),
        (0, False),
        (-1e100, False),
        (1e100, False),
    ],
)
def test_read_magic_number_first_line_is_number(text, expected):
    actual_result = read_magic_number(file_maker(text))
    os.remove("test_hw4_task1_sample.txt")
    assert actual_result == expected


@pytest.mark.parametrize(("text"), [([]), ("bac_cab"), ("")])
def test_read_magic_number_exception(text):
    with pytest.raises(ValueError, match="A very specific bad thing happened."):
        read_magic_number(file_maker(text))
    os.remove("test_hw4_task1_sample.txt")


def test_read_magic_number_file_not_exist():
    with pytest.raises(ValueError, match="A very specific bad thing happened."):
        read_magic_number("abubazeba.aka")
