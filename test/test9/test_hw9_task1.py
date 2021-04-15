"""TEST Homework 9.1."""
import os

import pytest

from hw.hw9.hw9_task1 import merge_sorted_files


@pytest.fixture()
def file_list():
    f1 = open("file1.txt", "w")
    f2 = open("file2.txt", "w")
    f3 = open("file3.txt", "w")

    f1.write("1\n100\n")
    f2.write("-4\n150\n")
    f3.write("3\n1200\n")

    f1.close()
    f2.close()
    f3.close()

    return ["file1.txt", "file2.txt", "file3.txt"]


def test_merge(file_list):
    actual_result = list(merge_sorted_files(file_list))
    for file in ("file1.txt", "file2.txt", "file3.txt"):
        os.remove(file)
    assert actual_result == [-4, 1, 3, 100, 150, 1200]
