"""
Classic task, a kind of walnut for you
Given four lists A, B, C, D of integer values,
    compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.
We guarantee, that all A, B, C, D have the same length of N where 0 ≤ N ≤ 1000.
"""
from typing import Dict, List


def count_list_elements(d: List[int]) -> Dict[int, int]:
    d_dict = {}
    for z in d:
        if z not in d_dict:
            d_dict[z] = 1
        else:
            d_dict[z] += 1
    return d_dict


def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    """Count how many combinations of elements, one from each list, exist
    such that the sum of these elements is 0."""
    zero_sums_count = 0
    d_dict = count_list_elements(d)
    for w in a:
        for x in b:
            wx = w + x
            for y in c:
                wxy = wx + y
                if -wxy in d_dict:
                    zero_sums_count += d_dict[-wxy]
    return zero_sums_count
