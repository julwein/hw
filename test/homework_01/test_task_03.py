from homework_01.task_03 import find_maximum_and_minimum


def test_12345():
    assert find_maximum_and_minimum("test/homework_01/test_task03_files/file0.txt") == (
        1,
        5,
    )


def test_0():
    assert find_maximum_and_minimum("test/homework_01/test_task03_files/file1.txt") == (
        0,
        0,
    )
