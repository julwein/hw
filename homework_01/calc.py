"""
task_01.md
Warming up
    1. please create your own git repository on github.
    2. (optional) setup pre-commit hook with black and isort formatting for the repo
    3. initialize .gitignore in the repository root (you can use this sample)
    4. create a homework1 directory in the repo
    5. then copy the sample_project into the directory.
    6. fix all bugs in the sample_project code
    7. write an extra test for each found bug
"""


def check_power_of_2(a: int) -> bool:
    """
     Return whether a is a positive integer power of 2.

     The idea is based on that bitwise a & (a-1) gives 0 when a is
    a non-negative integer power of 2.
    For example, for a = 8:
        1000
      & 0111
      = 0000
    Thus, bool(not (a & (a - 1))) gives True in this case.
    Besides, we should exclude the case of a = 0 which is not an integer power of 2,
    but 0 & -1 in two's-complement representation also gives 0:
        00...0
      & 11...1
      = 00...0,
    so we add "and a" to the expression.
    """
    return bool(not (a & (a - 1)) and a)
