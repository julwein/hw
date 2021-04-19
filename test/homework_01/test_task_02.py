from homework_01.task_02 import check_fibonacci, gen_fibonacci

"""Test gen_fibonacci"""


def test_gen_fibonacci_negative_inversed_order_arguments():
    assert gen_fibonacci(-1, -2) == []


def test_gen_fibonacci_0_5():
    assert gen_fibonacci(0, 5) == [0, 1, 1, 2, 3, 5]


def test_gen_fibonacci_0_1():
    assert gen_fibonacci(0, 1) == [0, 1, 1]


def test_gen_fibonacci_1_5():
    assert gen_fibonacci(1, 2) == [1, 1, 2]


def test_gen_fibonacci_1_1():
    assert gen_fibonacci(1, 1) == [1, 1]


"""Test check_fibonacci"""


def test_positive_case_from_0():
    """Testing that several consecutive Fibonacci numbers starting with 0 give True"""
    assert check_fibonacci([0, 1, 1, 2, 3, 5])


def test_positive_case_not_from_0():
    """Testing that Fibonacci subsequence not starting with 0 give True"""
    assert check_fibonacci([233, 377])


def test_positive_one_number():
    """Testing that a single Fibonacci number gives True"""
    assert check_fibonacci([1597])


def test_positive_0_1():
    """Testing that [0, 1] gives True"""
    assert check_fibonacci([0, 1])


def test_positive_0_1_1():
    """Testing that [0, 1, 1]"""
    assert check_fibonacci([0, 1, 1])


def test_negative_0_1_2():
    """Testing that [0, 1, 2] gives False"""
    assert not check_fibonacci([0, 1, 2])


def test_negative_case():
    """Testing that some not Fibonacci int sequence gives False"""
    assert not check_fibonacci([54, -65, -9])


def test_negative_empty():
    """Testing that empty sequence gives False"""
    assert not check_fibonacci([])


def test_negative_case_wrong_order():
    """Testing that a Fibonacci sequence with swapped elements gives False"""
    assert not check_fibonacci([13, 55, 34, 21, 89])
