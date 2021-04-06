"""TEST Homework 8.2."""
import pytest

from hw.hw8.hw8_task2 import TableData


@pytest.fixture()
def presidents():
    return TableData("example.sqlite", "presidents")


def test_len(presidents):
    assert len(presidents) == 3


def test_contains(presidents):
    assert "Vladimir Putin" in presidents


def test_not_contains(presidents):
    assert "Albert Gazaryan" not in presidents


def test_iter(presidents):
    presidents_names = [president["name"] for president in presidents]
    assert presidents_names == ["Joe Biden", "Vladimir Putin", "Xi Jinping"]
