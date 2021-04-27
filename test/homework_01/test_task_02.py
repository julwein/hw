from homework_01.task_02 import check_fibonacci, gen_fibonacci

"""Test gen_fibonacci"""


def test_gen_fibonacci_inversed_order_negative_arguments_return_empty_list():
    assert gen_fibonacci(-1, -2) == []


def test_gen_fibonacci_from_0_to_5():
    assert gen_fibonacci(0, 5) == [0, 1, 1, 2, 3, 5]


def test_gen_fibonacci_from_0_to_1_return_0_1_1():
    assert gen_fibonacci(0, 1) == [0, 1, 1]


def test_gen_fibonacci_from_1_to_2_return_1_1_2():
    assert gen_fibonacci(1, 2) == [1, 1, 2]


def test_gen_fibonacci_from_1_to_1_return_1_1():
    assert gen_fibonacci(1, 1) == [1, 1]


"""Test check_fibonacci"""


def test_positive_fib_sequence_from_0():
    assert check_fibonacci([0, 1, 1, 2, 3, 5])


def test_positive_fib_sequence_not_from_0():
    assert check_fibonacci([233, 377])


def test_positive_single_fib_number():
    assert check_fibonacci([1597])


def test_positive_0_1_sequence():
    assert check_fibonacci([0, 1])


def test_positive_0_1_1_sequence():
    assert check_fibonacci([0, 1, 1])


def test_negative_0_1_2_sequence():
    assert not check_fibonacci([0, 1, 2])


def test_negative_non_fib_sequence():
    assert not check_fibonacci([54, -65, -9])


def test_negative_single_non_fib_number():
    assert not check_fibonacci([1598])


def test_negative_empty_sequence():
    assert not check_fibonacci([])


def test_negative_fib_numbers_in_wrong_order():
    assert not check_fibonacci([13, 55, 34, 21, 89])
