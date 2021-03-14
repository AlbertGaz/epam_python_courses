"""Homework 4.1.

Read magic number from first line of the file.
"""


def read_magic_number(path: str) -> bool:
    """Read first line of file.

    Args:
        path: file path

    Returns: bool if first line is int and in [1,3)

    """
    try:
        with open(path, encoding="utf-8") as f:
            first_line = f.readline().strip()
        return 1 <= float(first_line) < 3
    except Exception:
        raise ValueError("A very specific bad thing happened.")
