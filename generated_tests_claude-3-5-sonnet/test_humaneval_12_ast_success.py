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
    (["a", "bb", "ccc"], "ccc"),
    (["hello", "hi", "hey"], "hello"),
    (["x", "xx", "x"], "xx"),
    (["abc", "def", "ghi"], "abc"),
    (["", "a", "ab"], "ab"),
    (["test", "testing", "te"], "testing"),
    ([], None),
    ([""], ""),
    (["a"], "a"),
    (["same", "dame", "fame"], "same"),
    (["  ", "    ", " "], "    "),
    (["a" * 10, "b" * 5, "c" * 10], "a" * 10),
    (["!@#", "$%^", "***"], "!@#"),
    (["line\n", "test", "multi\nline"], "multi\nline"),
    ([" ", "  ", "   "], "   ")
])
def test_longest_parametrized(input_list: List[str], expected: Optional[str]):
    assert longest(input_list) == expected

def test_longest_empty_list():
    assert longest([]) is None

def test_longest_single_element():
    assert longest(["test"]) == "test"

def test_longest_multiple_same_length():
    result = longest(["abc", "def", "ghi"])
    assert result in ["abc", "def", "ghi"]
    assert len(result) == 3

def test_longest_with_spaces():
    assert longest(["  ", " ", "   "]) == "   "

def test_longest_with_special_chars():
    assert longest(["!", "@@", "###"]) == "###"

def test_longest_unicode():
    assert longest(["α", "βγ", "δεζ"]) == "δεζ"

def test_longest_mixed_content():
    assert longest(["a1", "b22", "c333"]) == "c333"
