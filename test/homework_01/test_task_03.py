from homework_01.task_03 import find_maximum_and_minimum


def test_1_5():
    assert find_maximum_and_minimum("./test_task03_files/file0.txt") == (1, 5)


def test_0():
    assert find_maximum_and_minimum("./test_task03_files/file1.txt") == (0, 0)
