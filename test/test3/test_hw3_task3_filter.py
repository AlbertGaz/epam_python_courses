"""TEST Homework 3.3.

Correct from bugs script.
"""
import pytest

from hw.hw3.hw3_task3 import make_filter

sample_data = [
    {
        "name": "Bill",
        "last_name": "Gilbert",
        "occupation": "was here",
        "type": "person",
    },
    {"is_dead": True, "kind": "parrot", "type": "bird", "name": "polly"},
]


@pytest.mark.parametrize(
    ("arg", "expected_result"),
    [
        (
            {"name": "Bill"},
            [
                {
                    "name": "Bill",
                    "last_name": "Gilbert",
                    "occupation": "was here",
                    "type": "person",
                }
            ],
        ),
        (
            {"is_dead": True},
            [{"is_dead": True, "kind": "parrot", "type": "bird", "name": "polly"}],
        ),
        ({"name": "Bill", "is_dead": True}, []),
    ],
)
def test_make_filter(arg, expected_result):
    actual_result = make_filter(**arg).apply(sample_data)

    assert actual_result == expected_result
