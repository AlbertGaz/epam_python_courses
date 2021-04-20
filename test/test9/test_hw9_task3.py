"""TEST Homework 9.3."""

from hw.hw9.hw9_task3 import universal_file_counter


def test_universal_file_counter_none_tokenizer():
    actual_result = universal_file_counter("test/test9/test_hw9_task3_samples", "txt")
    assert actual_result == 12


def test_universal_file_counter_tokenizer():
    actual_result = universal_file_counter(
        "test/test9/test_hw9_task3_samples", "txt", str.split
    )
    assert actual_result == 19
