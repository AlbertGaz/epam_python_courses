"""Homework 2.1.

Analyze text.
"""
import string
from typing import List


def get_longest_diverse_words(file_path: str) -> List[str]:
    """Find 10 longest words with unique chars.

    Args:
        file_path: file to be analyzed directory

    Returns: max_words. list of 10 longest words

    """
    with open(file_path, encoding="utf-8") as f:
        max_words = ["" for _ in range(10)]
        for line in f:
            for word in line.split():
                for i in range(10):
                    if len(set(word)) > len(set(max_words[i])):
                        max_words[i] = word
                        max_words.sort(key=lambda x: len(set(x)))
                        break
        return max_words


def get_rarest_char(file_path: str) -> str:
    """Get rarest_char.

    Args:
        file_path: text file direction

    Returns: rarest char

    """
    with open(file_path, encoding="utf-8") as f:
        text = "".join(f.read().split())  # get rid of white space in text string
        text_chars = set(text)
        min_char_count = float("inf")
        for char in text_chars:
            if text.count(char) < min_char_count:
                min_char_count = text.count(char)
                min_char = char
    return min_char


def count_punctuation_chars(file_path: str) -> int:
    """Count punctuation.

    Args:
        file_path: file direction

    Returns: number of punctuations

    """
    with open(file_path, encoding="utf-8") as f:
        text = f.read()
        pncts = string.punctuation
        pnct_n = 0
        for pnct in pncts:
            pnct_n += text.count(pnct)
    return pnct_n


def count_non_ascii_chars(file_path: str) -> int:
    """Count non ascii.

    Args:
        file_path: file direction

    Returns: count of non ascii chars

    """
    with open(file_path, encoding="utf-8") as f:
        text = f.read()
        ascii_range = range(32, 256)
        non_ascii_count = 0
        for char in text:
            if ord(char) not in ascii_range:
                non_ascii_count += 1
    return non_ascii_count


def get_most_common_non_ascii_char(file_path: str) -> str:
    """Get most common non ascii char in file.

    Args:
        file_path: file to be parsed

    Returns: most common char

    """
    with open(file_path, encoding="utf-8") as f:
        text = f.read()
        ascii_range = range(32, 256)
        non_ascii = {}
        for char in text:
            if ord(char) not in ascii_range:
                non_ascii[char] = non_ascii.get(char, 0) + 1
    return sorted(non_ascii, key=non_ascii.get)[-1]
