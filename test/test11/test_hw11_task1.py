"""TEST Homework 11.1."""

import pytest

from hw.hw11.hw11_task1 import SimplifiedEnum


class ColorsEnum(metaclass=SimplifiedEnum):
    __keys = ("RED", "BLUE", "ORANGE", "BLACK")


class SizesEnum(metaclass=SimplifiedEnum):
    __keys = ("XL", "L", "M", "S", "XS")


@pytest.mark.parametrize(
    ("attr", "value"), [(ColorsEnum.RED, "RED"), (SizesEnum.XL, "XL")]
)
def test_simplified_enum(attr, value):
    assert attr == value
