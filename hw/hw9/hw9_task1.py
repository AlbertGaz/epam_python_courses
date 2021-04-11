"""Homework 9.1."""
from pathlib import Path
from typing import Iterator, List, Union


def merge_sorted_files(file_list: List[Union[Path, str]]) -> Iterator:
    """Merge integers from sorted files and returns an iterator. Fast, but memory needed."""
    files = [(open(file_name)).readlines() for file_name in file_list]
    elms = [el.strip() for line in files for el in line]
    yield from sorted(elms, key=lambda x: int(x))
