from homework_01.task_03 import find_maximum_and_minimum


def test_numbers_1_2_3_4_5_return_1_5():
    assert find_maximum_and_minimum("test/homework_01/test_task03_files/file0.txt") == (
        1,
        5,
    )


def test_numbers_0_return_0_0():
    assert find_maximum_and_minimum("test/homework_01/test_task03_files/file1.txt") == (
        0,
        0,
    )
