"""TEST Homework 3.2.

Test process parallelization.
"""
from hw.hw3.hw3_task2 import parallelized_slow_function


def test_slow_calculate():
    t_calc = parallelized_slow_function()
    assert t_calc < 60
