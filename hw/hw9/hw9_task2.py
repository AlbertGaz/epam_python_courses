"""Homework 9.2."""
from contextlib import contextmanager
from types import TracebackType


class Supressor:
    """Contex manager that supresses exceptions."""

    def __init__(self, err: Exception) -> None:
        self.err = err

    def __enter__(self) -> None:
        """Enter the runtime context related to this object."""
        pass

    def __exit__(
        self, exc_type: Exception, exc_value: Exception, traceback: TracebackType
    ) -> bool:
        """Exit the runtime context related to this object."""
        return isinstance(exc_value, self.err)


@contextmanager
def supressor_gen(err: Exception) -> None:
    """Contex manager that supresses exceptions."""
    try:
        yield
    except err:
        pass
