"""Homework 6.1."""
from typing import Any


def instances_counter(cls: Any) -> Any:
    """Create 2 methods to count and reset number of instances.

    Args:
        cls: class to add methods

    Returns: cls but with two new methods

    """
    cls.i = 0

    def init(self: Any) -> None:
        cls.i += 1

    @classmethod
    def get_created_instances(self: Any) -> int:
        """Return the instances count."""
        return cls.i

    def reset_instances_counter(self: Any) -> int:
        """Reset the instances count and return the last count."""
        old_i = cls.i
        cls.i = 0
        return old_i

    cls.__init__ = init
    cls.get_created_instances = get_created_instances
    cls.reset_instances_counter = reset_instances_counter
    return cls
