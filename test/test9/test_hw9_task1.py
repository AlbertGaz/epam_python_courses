"""TEST Homework 9.1."""
import os

import pytest

from hw.hw9.hw9_task1 import merge_sorted_files


def write_to_file(file_name, text):
    f = open(file_name, "w")
    f.write(text)
    f.close()


@pytest.fixture()
def file_list():

    write_to_file("file1.txt", "1\n100\n")
    write_to_file("file2.txt", "-4\n150\n")
    write_to_file("file3.txt", "3\n1200\n")

    return ["file1.txt", "file2.txt", "file3.txt"]


def test_merge(file_list):
    actual_result = list(merge_sorted_files(file_list))
    for file in ("file1.txt", "file2.txt", "file3.txt"):
        os.remove(file)
    assert actual_result == [-4, 1, 3, 100, 150, 1200]
