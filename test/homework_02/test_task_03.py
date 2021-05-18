from homework_02.task_03 import combinations


def test_one_input_list():
    assert list(combinations([1, 2])) == [[1], [2]]


def test_two_input_lists():
    assert list(combinations([1, 2], [3, 4])) == [
        [1, 3],
        [1, 4],
        [2, 3],
        [2, 4],
    ]
