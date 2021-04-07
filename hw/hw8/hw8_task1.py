"""Homework 8.1."""
from typing import Any, Union


class KeyValueStorage:
    """Class create object of storage, and we can get attributes of storage through . and []."""

    def __init__(self, filepath: str) -> None:
        self.dic = {}
        with open(filepath, "r") as f:
            text = f.read()
        for key, value in [pair.split("=") for pair in text.split()]:

            key, value = KeyValueStorage.is_int(key), KeyValueStorage.is_int(value)

            if isinstance(key, int):
                raise ValueError("Attribute cannot be an integer!")

            if key not in self.dic:
                self.dic[key] = value

    @classmethod
    def is_int(cls: Any, k_or_v: str) -> Union[int, str]:
        """Check if key is integer. If True - raises valueerror."""
        try:
            return int(k_or_v)
        except ValueError:
            return k_or_v

    def __getattr__(self, key: str) -> Union[str, int]:
        """Make it possible to get attribute by .."""
        if key in self.dic:
            return self.dic[key]
        raise AttributeError("Attribute not found!")

    def __getitem__(self, key: str) -> Union[int, str]:
        """Make it possible to get attribute by []."""
        if key in self.dic:
            return self.dic[key]
        raise KeyError("Key not found!")
