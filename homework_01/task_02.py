"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence
We guarantee, that the given sequence contains >= 0 integers inside.
"""
from typing import Sequence


def gen_fibonacci(beginning: int, end: int) -> Sequence[int]:
    """Generates Fibonacci sequence from 0 to a number less then or equal to n.
    NB! gen_fibonacci(0, 1) will return [0, 1, 1]
        gen_fibonacci(1, n) will return [1, 1, ..., k<=n]"""
    if beginning > end or beginning < 0 or end < 0:
        return []
    fib_seq = []
    f0, f1 = 0, 1
    while f0 <= end:
        if f0 >= beginning:
            fib_seq.append(f0)
        f0, f1 = f1, f0 + f1
    return fib_seq


def check_fibonacci(data: Sequence[int]) -> bool:
    """Return whether data is a subsequence of Fibonacci sequence"""
    if not data:
        return False
    beginning = data[0]
    end = data[-1]
    ref_seq = gen_fibonacci(beginning, end)
    # Remove duplicate 1 from ref_seq if there's only one 1 in data and
    # it's at the beginning or at the end of the data list:
    if (data.count(1) == 1) and (beginning == 1 or end == 1) and (1 in ref_seq):
        ref_seq.remove(1)
    return data == ref_seq
