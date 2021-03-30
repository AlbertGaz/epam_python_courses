"""Homework 7.1."""
from typing import Any


def find_occurrences(tree: dict, element: Any) -> int:
    """Find value occurrences of element in nested structures."""
    count = 0
    if isinstance(tree, dict):
        for key in tree:
            count += find_occurrences(tree[key], element)
    elif isinstance(tree, (list, tuple)):
        for key in tree:
            count += find_occurrences(key, element)
    elif isinstance(tree, set) and element in tree:
        count += 1
    else:
        if tree == element:
            count += 1
    return count
