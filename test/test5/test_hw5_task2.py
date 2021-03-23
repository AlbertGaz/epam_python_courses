"""TEST Homework 5.2."""
import functools
import sys

import pytest

from hw.hw5.hw5_task2 import wraps


def print_result(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """Function-wrapper which print result of an original function."""
        result = func(*args, **kwargs)
        sys.stdout.write(str(result))
        return result

    return wrapper


@print_result
def custom_sum(*args):
    """Sum any objects which have __add__."""
    return functools.reduce(lambda x, y: x + y, args)


@pytest.mark.parametrize(
    ("args", "expected_result"),
    [([[1, 2, 3], [4, 5]], [1, 2, 3, 4, 5]), ([1, 2, 3, 4], 10)],
)
def test_result(args, expected_result):
    actual_result = custom_sum(*args)
    assert actual_result == expected_result


@pytest.mark.parametrize(
    ("atr", "expected_result"),
    [
        (
            custom_sum.__doc__,
            """This function can sum any objects which have __add___""",
        ),
        (custom_sum.__name__, "custom_sum"),
    ],
)
def test_doc_name(atr, expected_result):
    assert atr == expected_result


def test_stdout(capsys):
    custom_sum(1, 2, 3, 4)
    out, _ = capsys.readouterr()
    assert out == "10"

    without_print = custom_sum.__original_func
    without_print(1, 2, 3, 4)
    out, _ = capsys.readouterr()
    assert out == ""
