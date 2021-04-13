"""Homework 9.3."""
import os
from pathlib import Path
from typing import Callable, Optional


def universal_file_counter(
    dir_path: Path, file_extension: str, tokenizer: Optional[Callable] = None
) -> int:
    """Count lines or tokens in all files with that extension."""
    file_name_list = os.listdir(dir_path)
    files_true_ext = [
        open(str(dir_path) + "\\" + file)
        for file in file_name_list
        if file.endswith(file_extension)
    ]
    if not tokenizer:
        return len([row for f in files_true_ext for row in f.readlines()])
    return len(
        [
            token
            for f in files_true_ext
            for row in f.readlines()
            for token in tokenizer(row)
        ]
    )
