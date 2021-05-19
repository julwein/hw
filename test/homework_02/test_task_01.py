"""
Test functions from task_01.py on small file 'test_paragraph.txt'.
"""


from homework_02.task_01 import (
    count_non_ascii_chars,
    count_punctuation_chars,
    get_longest_diverse_words,
    get_most_common_non_ascii_char,
    get_rarest_char,
)


def test_get_longest_diverse_words():
    assert get_longest_diverse_words("test/homework_02/test_paragraph.txt") == [
        "ausführen",
        "hinter",
        "gefaßt",
        "machen",
        "Titel",
        "nicht",
        "Pfade",
        "sich",
        "chen",
        "über",
    ]


def test_get_longest_diverse_words_n_2():
    assert get_longest_diverse_words("test/homework_02/test_paragraph.txt", n=2) == [
        "ausführen",
        "hinter",
    ]


def test_get_rarest_char():
    assert get_rarest_char("test/homework_02/test_paragraph.txt") == "1"


def test_count_punctuation_chars():
    assert count_punctuation_chars("test/homework_02/test_paragraph.txt") == 8


def test_count_non_ascii_chars():
    assert count_non_ascii_chars("test/homework_02/test_paragraph.txt") == 6


def test_get_most_common_non_ascii_char():
    assert get_most_common_non_ascii_char("test/homework_02/test_paragraph.txt") == "ü"
