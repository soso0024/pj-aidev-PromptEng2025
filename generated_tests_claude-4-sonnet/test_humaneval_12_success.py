# Test cases for HumanEval/12
# Generated using Claude API

from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    >>> longest([])

    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    """

    if not strings:
        return None

    maxlen = max(len(x) for x in strings)
    for s in strings:
        if len(s) == maxlen:
            return s


# Generated test cases:
import pytest
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None

    maxlen = max(len(x) for x in strings)
    for s in strings:
        if len(s) == maxlen:
            return s

def test_empty_list():
    assert longest([]) is None

def test_single_string():
    assert longest(["hello"]) == "hello"

def test_multiple_strings_different_lengths():
    assert longest(["a", "bb", "ccc"]) == "ccc"

def test_multiple_strings_same_length():
    assert longest(["abc", "def", "ghi"]) == "abc"

def test_longest_at_beginning():
    assert longest(["longest", "a", "bb"]) == "longest"

def test_longest_at_end():
    assert longest(["a", "bb", "longest"]) == "longest"

def test_longest_in_middle():
    assert longest(["a", "longest", "bb"]) == "longest"

def test_empty_strings():
    assert longest(["", "", ""]) == ""

def test_mix_empty_and_non_empty():
    assert longest(["", "a", ""]) == "a"

def test_single_character_strings():
    assert longest(["a", "b", "c"]) == "a"

def test_very_long_string():
    long_string = "a" * 1000
    assert longest([long_string, "short"]) == long_string

def test_unicode_strings():
    assert longest(["café", "naïve", "résumé"]) == "résumé"

def test_special_characters():
    assert longest(["!@#", "$%^&", "*"]) == "$%^&"

def test_whitespace_strings():
    assert longest([" ", "  ", "   "]) == "   "

def test_newline_characters():
    assert longest(["a\n", "b\n\n", "c"]) == "b\n\n"

@pytest.mark.parametrize("strings,expected", [
    (["a"], "a"),
    (["short", "medium", "very_long"], "very_long"),
    (["same", "size"], "same"),
    (["", "x"], "x"),
    (["123", "45", "6789"], "6789")
])
def test_parametrized_cases(strings, expected):
    assert longest(strings) == expected