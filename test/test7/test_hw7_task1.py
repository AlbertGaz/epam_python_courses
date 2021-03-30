"""TEST Homework 7.1."""
import pytest

from hw.hw7.hw7_task1 import find_occurrences


example_tree_from_task_description = {
    "first": ["RED", "BLUE"],
    "second": {
        "simple_key": ["simple", "list", "of", "RED", "valued"],
    },
    "third": {
        "abc": "BLUE",
        "jhl": "RED",
        "complex_key": {
            "key1": "value1",
            "key2": ["RED"],
            "key3": ["a", "lot", "of", "values", {"nested_key": ["RED"]}],
        },
    },
    "fourth": "RED",
}

example_tree1 = {
    1: "RED",
    2: {"RED"},
    3: ["RED", ["RED", ["RED", ["RED", {4: "RED"}]]]],
    5: {6: {7: {8: {9: {10: ["RED", "RED", "RED"]}}}}},
}


@pytest.mark.parametrize(
    ("tree", "element", "expected_result"),
    [
        (example_tree_from_task_description, "RED", 6),
        (example_tree1, "RED", 10),
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
