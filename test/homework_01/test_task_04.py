from homework_01.task_04 import check_sum_of_four


def test_lists_length_0_return_0():
    assert check_sum_of_four([], [], [], []) == 0


def test_lists_length_1_return_1():
    assert check_sum_of_four([1], [1], [-1], [-1]) == 1


def test_lists_length_1_return_0():
    assert check_sum_of_four([0], [1], [-1], [-1]) == 0


def test_lists_length_2_return_8():
    assert check_sum_of_four([0, 1], [1, 1], [-1, -1], [-1, -1]) == 8
