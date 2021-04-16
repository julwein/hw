"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence
We guarantee, that the given sequence contains >= 0 integers inside.
"""
from typing import Sequence


def gen_fibonacci(n: int) -> Sequence[int]:
    """Generates Fibonacci sequence from 0 to a number less then or equal to n.
    NB! If n == 1, the function will return [0, 1, 1]"""
    if n < 0:
        return []
    fib_seq = []
    f0, f1 = 0, 1
    while f0 <= n:
        fib_seq.append(f0)
        f0, f1 = f1, f0 + f1
    return fib_seq


def check_fibonacci(data: Sequence[int]) -> bool:
    if not data:
        return False
    if data == [0, 1]:
        return True
    n = data[-1]
    reference_seq = gen_fibonacci(n)
    if len(data) > len(reference_seq):
        return False
    for element in reversed(data):
        ref_number = reference_seq.pop()
        if element != ref_number:
            return False
    return True
