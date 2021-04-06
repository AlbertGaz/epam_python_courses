"""TEST Homework 8.1."""
import pytest

from hw.hw8.hw8_task1 import KeyValueStorage

storage1 = KeyValueStorage("test/test8/hw8_task1_example.txt")


@pytest.mark.parametrize(
    ("att", "expected"),
    [
        (storage1.name, "kek"),
        (storage1.a1, 1),
        (storage1.song_name, "shadilay"),
        (storage1.power, 9001),
    ],
)
def test_key_value_storage_attr(att, expected):
    assert att == expected


@pytest.mark.parametrize(
    ("att", "expected"),
    [("name", "kek"), ("a1", 1), ("song_name", "shadilay"), ("power", 9001)],
)
def test_key_value_storage_item(att, expected):
    assert storage1[att] == expected


def test_key_value_storage_with_exceptions():
    with pytest.raises(ValueError, match="Attribute cannot be an integer"):
        KeyValueStorage("test/test8/hw8_task1_example_with_exceptions.txt")
