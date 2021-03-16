"""TEST Homework 4.2.

Check function count_dots_on_i
"""
from unittest.mock import patch

import pytest

from hw.hw4.hw4_task2 import count_dots_on_i


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("iii", 3),
        ("i1i2i3 no more i (oh, one more)", 4),
        ("", 0),
        ("I has no dot, not like i, so here we have two dots", 2),
    ],
)
def test_count_dots_on_i_existing_url(text, expected):
    with patch("requests.get") as mock_request:
        mock_request.return_value.text = text
        actual_result = count_dots_on_i("existing_url")
        assert actual_result == expected


def test_count_dots_on_i_not_existing_url():
    with patch("requests.get") as mock_request:
        mock_request.side_effect = Exception
        with pytest.raises(ValueError, match="Unreachable not_existing_url"):
            count_dots_on_i("not_existing_url")
