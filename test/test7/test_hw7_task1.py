"""TEST Homework 7.1."""
import json

import pytest

from hw.hw7.hw7_task1 import find_occurrences


@pytest.fixture()
def example_tree():
    with open("example_tree.txt", "r") as f:
        return json.loads(f.read())


@pytest.mark.parametrize(
    ("tree", "element", "expected_result"),
    [
        ([], "RED", 0),
        ({}, "RED", 0),
        (True, True, 1),
        (1, 1, 1),
        (["a", "a"], "a", 2),
    ],
)
def test_find_occurrences(tree, element, expected_result):
    actual_result = find_occurrences(tree, element)
    assert actual_result == expected_result


def test_find_occurrences_example_tree(example_tree):
    actual_result = find_occurrences(example_tree, "RED")
    assert actual_result == 6
