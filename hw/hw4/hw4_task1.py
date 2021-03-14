"""Homework 4.1.

Read magic number from first line of the file.
"""


def read_magic_number(path: str) -> bool:
    """Read first line of file.

    Args:
        path: file path

    Returns: bool if first line is int and in [1,3)

    """
    with open(path, encoding="utf-8") as f:
        first_line = f.readline().strip()
    return 1 <= float(first_line) < 3
