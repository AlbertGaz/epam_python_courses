"""Homework 9.1."""
from pathlib import Path
from typing import Iterator, List, Union


def get_int_from_file(file: Union[Path, str]) -> Iterator:
    """Give a single integer from file."""
    with open(file) as f:
        while row := f.readline():
            yield int(row.strip())


def merge_sorted_files(file_list: List[Union[Path, str]]) -> Iterator:
    """Merge integers from sorted files and returns an iterator."""
    files_int_gen = [get_int_from_file(file) for file in file_list]
    dic = {}
    inf = float("inf")
    for i, gen in enumerate(files_int_gen):
        dic[f"f{i}"] = [gen, next(gen)]
    while True:
        key_min_value = min(dic, key=lambda x: dic[x][1])
        min_value = dic[key_min_value][1]
        if min_value == inf:
            break
        yield min_value
        try:
            dic[key_min_value][1] = next(dic[key_min_value][0])
        except StopIteration:
            dic[key_min_value][1] = inf
