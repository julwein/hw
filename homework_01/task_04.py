"""
Classic task, a kind of walnut for you
Given four lists A, B, C, D of integer values,
    compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.
We guarantee, that all A, B, C, D have the same length of N where 0 ≤ N ≤ 1000.
"""
from typing import Dict, List


def count_2_lists_element_sums(a: List[int], b: List[int]) -> Dict[int, int]:
    """Count various sums of elements from two lists,
    one element from each list."""
    ab_sums_dict = {}
    for x in a:
        for y in b:
            if x + y not in ab_sums_dict:
                ab_sums_dict[x + y] = 1
            else:
                ab_sums_dict[x + y] += 1
    return ab_sums_dict


def count_zero_sums_of_four(
    a: List[int], b: List[int], c: List[int], d: List[int]
) -> int:
    """Count how many combinations of elements, one from each of 4 lists, exist
    such that the sum of these elements is 0."""
    zero_sums_count = 0
    ab_sums = count_2_lists_element_sums(a, b)
    cd_sums = count_2_lists_element_sums(c, d)
    for ab in ab_sums:
        if -ab in cd_sums:
            zero_sums_count += ab_sums[ab] * cd_sums[-ab]
    return zero_sums_count
