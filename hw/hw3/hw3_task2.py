"""Homework 3.2.

Using multiprocessing optimize function work.
"""
import hashlib
import random
import struct
import time
from multiprocessing import Pool


def slow_calculate(value: int) -> int:
    """Do some weird voodoo magic calculations."""
    time.sleep(random.randint(1, 3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack("<" + "B" * len(data), data))


def parallelized_slow_function() -> float:
    """Parallelized slow_function.

    Returns: computation time.
    """
    t_start = time.time()
    num_processors = 60
    p = Pool(num_processors)
    p.map(slow_calculate, list(range(0, 500)))
    return time.time() - t_start
