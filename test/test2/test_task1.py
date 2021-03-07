"""TEST Homework 2.1.

Check correctness of function parsing text file.
"""
import pytest

from hw.hw2.task1 import count_non_ascii_chars
from hw.hw2.task1 import count_punctuation_chars
from hw.hw2.task1 import get_longest_diverse_words
from hw.hw2.task1 import get_most_common_non_ascii_char
from hw.hw2.task1 import get_rarest_char


@pytest.mark.parametrize(
    ("file_path", "expected_result"),
    [
        (
            "test/test2/test_samples_task1/test_task1_sample1.txt",
            [
                "asd",
                "sdaf",
                "1234",
                "bsfddsfaf",
                "4567g",
                "987654",
                "fdsgjl?']",
                "/>,pfdvgbtn+-fdvbr",
                "1234567890abcdefghigklmnop",
                "wertyuiop';lkjhgfdsazxcvbnm,./`~+_)(*&^%$#@!",
            ],
        ),
        (
            "test/test2/test_samples_task1/test_task1_sample2.txt",
            ["", "", "", "", "", "", "", "", "", ""],
        ),
    ],
)
def test_get_longest_diverse_words(file_path: str, expected_result: list):
    actual_result = get_longest_diverse_words(file_path)

    assert actual_result == expected_result


@pytest.mark.parametrize(
    ("file_path", "expected_result"),
    [
        ("test/test2/test_samples_task1/test_task1_sample3.txt", "w"),
    ],
)
def test_get_rarest_char(file_path: str, expected_result: str):
    actual_result = get_rarest_char(file_path)

    assert actual_result == expected_result


@pytest.mark.parametrize(
    ("file_path", "expected_result"),
    [
        ("test/test2/test_samples_task1/test_task1_sample4.txt", 20),
    ],
)
def test_count_punctuation_chars(file_path: str, expected_result: int):
    actual_result = count_punctuation_chars(file_path)

    assert actual_result == expected_result


@pytest.mark.parametrize(
    ("file_path", "expected_result"),
    [
        ("test/test2/test_samples_task1/test_task1_sample5.txt", 6),
    ],
)
def test_count_non_ascii_chars(file_path: str, expected_result: int):
    actual_result = count_non_ascii_chars(file_path)

    assert actual_result == expected_result


@pytest.mark.parametrize(
    ("file_path", "expected_result"),
    [
        ("test/test2/test_samples_task1/test_task1_sample6.txt", "䃘"),
    ],
)
def test_get_most_common_non_ascii_char(file_path: str, expected_result: str):
    actual_result = get_most_common_non_ascii_char(file_path)

    assert actual_result == expected_result
