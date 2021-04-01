"""Homework 8.1."""
from typing import Any, Union


class KeyValueStorage:
    """Class create object of storage, and we can get attributes of storage through . and []."""

    def __init__(self, filepath: str) -> None:
        self.dic = {}
        with open(filepath, "r") as f:
            text = f.read()
        for key, value in [pair.split("=") for pair in text.split()]:
            KeyValueStorage.check_is_key_int(key)
            value = KeyValueStorage.make_value_an_int_if_needed(value)
            if key not in self.dic:
                self.dic[key] = value

    @classmethod
    def check_is_key_int(cls: Any, key: str) -> None:
        """Check if key is integer. If True - raises valueerror."""
        try:
            key = int(key)
        except ValueError:
            pass

        if isinstance(key, int):
            raise ValueError("Attribute cannot be an integer!")

    @classmethod
    def make_value_an_int_if_needed(cls: Any, value: str) -> Union[int, str]:
        """Return int type of value if it is int in str, else return str value."""
        try:
            return int(value)
        except ValueError:
            return value

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
