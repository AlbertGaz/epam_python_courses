"""Homework 11.1."""

from typing import Dict, Tuple


class SimplifiedEnum(type):
    """Remove duplications in variables declarations using metaclasses."""

    def __new__(cls, name: str, bases: Tuple, dct: Dict):
        """Set attributes as in enum to instance classes."""
        cls_instance = super().__new__(cls, name, bases, dct)
        for attr in dct[f"_{name}__keys"]:
            setattr(cls_instance, attr, attr)
        return cls_instance
