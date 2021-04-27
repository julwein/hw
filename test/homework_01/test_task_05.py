from homework_01.task_05 import find_maximal_subarray_sum


def test_nums_3_2_1_k_1_return_3():
    assert find_maximal_subarray_sum([3, 2, 1], 1) == 3


def test_nums_3_2_1_k_10_return_6():
    assert find_maximal_subarray_sum([3, 2, 1], 10) == 6
