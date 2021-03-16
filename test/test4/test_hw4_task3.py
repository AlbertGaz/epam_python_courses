"""TEST Homework 4.3."""
import pytest

from hw.hw4.hw4_task3 import my_precious_logger


@pytest.mark.parametrize(("text"), [("error"), ("error: bad bad code")])
def test_my_precious_logger_stderr(capsys, text):
    my_precious_logger(text)
    captured = capsys.readouterr()
    assert captured.err == text


@pytest.mark.parametrize(("text"), [("1error"), ("Error: bad bad code")])
def test_my_precious_logger_stdout(capsys, text):
    my_precious_logger(text)
    captured = capsys.readouterr()
    assert captured.out == text
