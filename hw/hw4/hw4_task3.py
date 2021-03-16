"""Homework 4.3.

Write to stderr and stdout.
"""
import sys


def my_precious_logger(text: str) -> None:
    """Write to stdout or stderr if starts with "error".

    Args:
        text: text to be printed

    Returns: write to stderr if starts with error, else to stdout

    """
    dataflow = sys.stderr if text.startswith("error") else sys.stdout
    dataflow.write(text)
