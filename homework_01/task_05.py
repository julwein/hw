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
    k = min(k, len(nums))  # in case k > len(nums)
    for m in range(1, k + 1):  # m - various subarray lengths = sliding window width
        s = sum(nums[:m])  # s - initial sum of elements inside the sliding window
        if s > max_sum:
            max_sum = s
        for i in range(1, len(nums) - m + 1):
            # i - position of the first element of the sliding window
            s = s - nums[i - 1] + nums[i + m - 1]
            if s > max_sum:
                max_sum = s
    return max_sum
