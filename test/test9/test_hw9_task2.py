"""TEST Homework 9.2."""
import pytest

from hw.hw9.hw9_task2 import Supressor, supressor_gen


def test_supressor_class_good():
    with Supressor(ValueError):
        raise ValueError


def test_supressor_class_bad():
    contex_manager = Supressor(ValueError)
    with pytest.raises(ZeroDivisionError):
        with contex_manager:
            raise ZeroDivisionError


def test_supressor_gen_good():
    with supressor_gen(ValueError):
        raise ValueError


def test_supressor_gen_bad():
    with pytest.raises(ZeroDivisionError):
        with supressor_gen(ValueError):
            raise ZeroDivisionError
