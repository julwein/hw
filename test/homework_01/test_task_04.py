from homework_01.task_04 import count_2_lists_element_sums, count_zero_sums_of_four


def test_count_2_lists_element_sums():
    assert count_2_lists_element_sums([1, 1], [1, -1]) == {2: 2, 0: 2}


def test_count_zero_sums_of_four_lists_length_0_return_0():
    assert count_zero_sums_of_four([], [], [], []) == 0


def test_count_zero_sums_of_four_lists_length_1_return_1():
    assert count_zero_sums_of_four([1], [1], [-1], [-1]) == 1


def test_count_zero_sums_of_four_lists_length_1_return_0():
    assert count_zero_sums_of_four([0], [1], [-1], [-1]) == 0


def test_count_zero_sums_of_four_lists_length_2_return_8():
    assert count_zero_sums_of_four([0, 1], [1, 1], [-1, -1], [-1, -1]) == 8
