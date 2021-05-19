from homework_02.task_02 import major_and_minor_elem


def test_3_2_3_return_3_2():
    assert major_and_minor_elem([3, 2, 3]) == (3, 2)


def test_2_2_1_1_1_2_2_return_2_1():
    assert major_and_minor_elem([2, 2, 1, 1, 1, 2, 2]) == (2, 1)


def test_42_return_42_42():
    assert major_and_minor_elem([42]) == (42, 42)
