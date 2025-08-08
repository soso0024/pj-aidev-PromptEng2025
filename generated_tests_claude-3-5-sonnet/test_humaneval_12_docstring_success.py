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


@pytest.mark.parametrize("input_list,expected", [
    ([], None),
    (["a"], "a"),
    (["a", "b", "c"], "a"),
    (["a", "bb", "ccc"], "ccc"),
    (["aaa", "bbb", "ccc"], "aaa"),
    (["", "a", "bb"], "bb"),
    (["hello", "world", "python"], "python"),
    (["abc", "def", "ghi"], "abc"),
    (["x" * 10, "y" * 5, "z" * 2], "x" * 10),
    (["", "", ""], ""),
])
def test_longest_parametrized(input_list: List[str], expected: Optional[str]):
    assert longest(input_list) == expected


def test_longest_empty_list():
    assert longest([]) is None


def test_longest_single_element():
    assert longest(["test"]) == "test"


def test_longest_same_length():
    assert longest(["abc", "def", "ghi"]) == "abc"


def test_longest_with_empty_strings():
    assert longest(["", "a", ""]) == "a"


def test_longest_special_characters():
    assert longest(["@#$", "!", "12345"]) == "12345"


def test_longest_whitespace():
    assert longest(["  ", " ", "   "]) == "   "


def test_longest_unicode():
    assert longest(["α", "βγ", "δεζ"]) == "δεζ"
