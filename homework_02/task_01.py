"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
from collections import Counter, namedtuple
from typing import List
from unicodedata import category

Token = namedtuple("Token", ["token_type", "value"])


def tokenize(file_path: str, encoding: str = "unicode-escape"):
    """
    Open text file and create generator for text elements of four categories - word,
    symbol, punctuation, non-ascii, - as tuples (category, element).
    """
    with open(file_path, encoding=encoding) as data:
        symb = data.read(1)
        word = ""
        while symb:
            yield Token("symbol", symb)

            if category(symb).startswith("L"):
                word += symb
            else:
                if word:
                    yield Token("word", word)
                    word = ""

            if category(symb).startswith("P"):
                yield Token("punctuation", symb)

            if not symb.isascii():
                yield Token("non-ascii", symb)

            symb = data.read(1)


def is_diverse(word):
    return len(set(word)) == len(word)


def get_longest_diverse_words(
    file_path: str, *, encoding: str = "unicode-escape", n: int = 10
) -> List[str]:
    """
    Find n longest words consisting from largest amount of unique symbols from a file.
    """
    longest_words = [""] * n
    for token_type, word in tokenize(file_path, encoding):
        if (
            token_type == "word"
            and is_diverse(word)
            and len(word) > len(longest_words[-1])
            and word not in longest_words
        ):
            longest_words[-1] = word
            longest_words.sort(key=len, reverse=True)
    return longest_words


def get_rarest_char(file_path: str, encoding: str = "unicode-escape") -> str:
    """
    Find rarest symbol for document.
    """
    chars = [
        symb
        for token_type, symb in tokenize(file_path, encoding)
        if token_type == "symbol"
    ]
    char_counter = Counter(chars)
    n_min = len(chars)
    for symb, n in char_counter.items():
        if n < n_min:
            symb_min = symb
            n_min = n
    return symb_min


def count_punctuation_chars(file_path: str, encoding: str = "unicode-escape") -> int:
    """
    Count every punctuation char.
    """
    count = 0
    for token_type, _symb in tokenize(file_path, encoding):
        if token_type == "punctuation":
            count += 1
    return count


def count_non_ascii_chars(file_path: str, encoding: str = "unicode-escape") -> int:
    """
    Count every punctuation char.
    """
    count = 0
    for token_type, _symb in tokenize(file_path, encoding):
        if token_type == "non-ascii":
            count += 1
    return count


def get_most_common_non_ascii_char(
    file_path: str, encoding: str = "unicode-escape"
) -> str:
    """
    Find most common non-ascii char for document.
    """
    symb_counter = Counter(
        [
            symb
            for token_type, symb in tokenize(file_path, encoding)
            if token_type == "non-ascii"
        ]
    )
    n_max = 0
    for symb, n in symb_counter.items():
        if n > n_max:
            symb_max = symb
            n_max = n
    return symb_max
