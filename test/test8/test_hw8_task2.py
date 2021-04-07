"""TEST Homework 8.2."""
import pytest

from hw.hw8.hw8_task2 import TableData


@pytest.fixture()
def presidents():
    return TableData("test/test8/example.sqlite", "presidents")


def test_len(presidents):
    assert len(presidents) == 3


def test_contains(presidents):
    assert "Vladimir Putin" in presidents


def test_not_contains(presidents):
    assert "Albert Gazaryan" not in presidents


def test_item_exist(presidents):
    assert presidents["Vladimir Putin"] == (
        "Vladimir Putin",
        "Russian Federation",
        2000,
    )


def test_item_dont_exist(presidents):
    with pytest.raises(KeyError, match="Key Albert Gazaryan not found"):
        presidents["Albert Gazaryan"]


def test_iter(presidents):
    presidents_names = [president["name"] for president in presidents]
    assert presidents_names == ["Joe Biden", "Vladimir Putin", "Xi Jinping"]
