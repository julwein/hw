from homework_01.task_02 import check_fibonacci


def test_positive_case_from_0():
    """Testing that several consecutive Fibonacci numbers starting with 0 give True"""
    assert check_fibonacci([0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377])


def test_positive_case_not_from_0():
    """Testing that several consecutive Fibonacci numbers not starting with 0 give True"""
    assert check_fibonacci([233, 377])


def test_positive_one_number():
    """Testing that a single Fibonacci number gives True"""
    assert check_fibonacci([1597])


def test_positive_0_1():
    """Testing that [0, 1] gives True"""
    assert check_fibonacci([0, 1])


def test_negative_case():
    """Testing that some not Fibonacci int sequence gives False"""
    assert not check_fibonacci([54, -65, -9])


def test_negative_empty():
    """Testing that empty sequence gives False"""
    assert not check_fibonacci([])


def test_negative_case_wrong_order():
    """Testing that a Fibonacci sequence with swapped elements gives False"""
    assert not check_fibonacci([1, 2, 3, 5, 8, 13, 55, 34, 21, 89, 144])


def test_negative_case_wrong_last_el():
    """Testing that a Fibonacci sequence with two swapped elements including
    the last one gives False"""
    assert not check_fibonacci([1, 2, 3, 5, 8, 21, 34, 55, 89, 144, 13])
