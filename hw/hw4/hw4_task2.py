"""Homework 4.2.

Function count letters "i" in HTML page by url.
"""
import requests


def count_dots_on_i(url: str) -> int:
    """Count letters i with dot.

    Args:
        url: url to html page

    Returns: number of i in this html page

    """
    try:
        html = requests.get(url)
        return html.text.count("i")
    except Exception:
        raise ValueError(f"Unreachable {url}")
