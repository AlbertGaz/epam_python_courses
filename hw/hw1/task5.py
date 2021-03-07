"""Homework 1.5.

Given a list of integers numbers "nums".
You need to find a sub-array with length less equal to "k", with maximal sum.
The written function should return the sum of this sub-array.
"""
from typing import List


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    """Find maximal subarray.

    Args:
        nums: list
        k: int

    Returns: int

    """
    max_sub = -float("inf")
    for j in range(1, k + 1):
        for i in range(len(nums) - (j - 1)):
            if sum(nums[i : i + j]) > max_sub:
                max_sub = sum(nums[i : i + j])
    return max_sub
