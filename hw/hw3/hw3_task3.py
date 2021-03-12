"""Homework 3.3.

Correct script.
"""

from functools import partial


class Filter:
    """Filter class.

    Accepts a list of single-argument
    functions that return True if object in list conforms to some criteria
    """

    def __init__(self, *functions: list):
        self.functions = functions

    def apply(self, data: list) -> list:
        """Filter method.

        Args:
            data: list

        Returns: list

        """
        return [item for item in data if all((i(item) for i in self.functions))]


def make_filter(**keywords: dict) -> callable:
    """Generate filter object for specified keywords."""
    filter_funcs = []
    for key, value in keywords.items():

        def keyword_filter_func(key: str, value: str, dic: dict) -> callable:
            if key not in dic.keys():
                return False
            return dic[key] == value

        filter_funcs.append(partial(keyword_filter_func, key, value))
    return Filter(*filter_funcs)
