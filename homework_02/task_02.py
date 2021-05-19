"""
Given an array of size n, find the most common and the least common elements.
The most common element is the element that appears more than n // 2 times.
The least common element is the element that appears fewer than others.
You may assume that the array is non-empty and the most common element
always exist in the array.
Example 1:
Input: [3,2,3]
Output: 3, 2
Example 2:
Input: [2,2,1,1,1,2,2]
Output: 2, 1
"""
from collections import Counter
from typing import List, Tuple


def major_and_minor_elem(inp: List[int]) -> Tuple[int, int]:
    """
    Return tuple (most_common_element, least_common_element).
    """
    el_occurance = Counter(inp)
    most_common_el = inp[0]
    least_common_el = inp[0]
    for el, n in el_occurance.items():
        if n > el_occurance[most_common_el]:
            most_common_el = el
        if n < el_occurance[least_common_el]:
            least_common_el = el
    return most_common_el, least_common_el
