"""TEST Homework 9.1."""
import os

import pytest

from hw.hw9.hw9_task1 import merge_sorted_files


@pytest.fixture()
def file_list():
    with open("file1.txt", "w") as f1, open("file2.txt", "w") as f2, open(
        "file3.txt", "w"
    ) as f3:
        f1.write("1\n4\n7\n10\n")
        f2.write("2\n5\n8\n11\n")
        f3.write("3\n6\n9\n12\n")
    return ["file1.txt", "file2.txt", "file3.txt"]


def test_merge(file_list):
    actual_result = list(merge_sorted_files(file_list))
    os.remove("file1.txt")
    os.remove("file2.txt")
    os.remove("file3.txt")
    assert actual_result == [
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "11",
        "12",
    ]
