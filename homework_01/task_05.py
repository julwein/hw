"""
Given a list of integers numbers "nums".
You need to find a sub-array with length less equal to "k", with maximal sum.
The written function should return the sum of this sub-array.
Examples:
    nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    result = 16
"""
from typing import List


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    """
    Return maximum possible sum of elements of nums subarray with length less then or equal to k.
    nums list must not be empty. k must be > 0.
    """
    max_sum = nums[0]
    max_subarr_len = min(k, len(nums))
    for i in range(1, max_subarr_len + 1):
        for n in range(len(nums) - i + 1):
            if sum(nums[n : n + i]) > max_sum:
                max_sum = sum(nums[n : n + i])
    return max_sum
