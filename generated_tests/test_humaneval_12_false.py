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
from longest import longest

@pytest.mark.parametrize("test_input,expected", [
    (["a", "ab", "abc"], "abc"),
    (["hello", "world", "python"], "python"),
    (["", "a", "aa"], "aa"),
    (["test"], "test"),
    ([], None),
    (["", "", ""], ""),
    (["abc", "def", "ghi"], "abc"),
    (["short", "longer", "longest"], "longest"),
    (["same", "size", "text"], "same"),
    ([" ", "a", "  "], "  "),
    (["!@#", "123", "abc"], "!@#"),
    (["a" * 10, "b" * 5, "c" * 2], "a" * 10),
    (["", "empty", ""], "empty"),
    ([" ", "\t", "\n"], "\t"),
])
def test_longest_parametrized(test_input: List[str], expected: Optional[str]):
    assert longest(test_input) == expected

def test_longest_with_none_value():
    with pytest.raises(TypeError):
        longest(None)

def test_longest_with_non_list():
    with pytest.raises(TypeError):
        longest("not a list")

def test_longest_with_non_string_elements():
    with pytest.raises(TypeError):
        longest([1, 2, 3])

def test_longest_with_mixed_types():
    with pytest.raises(TypeError):
        longest(["string", 123, "another"])

def test_longest_with_special_characters():
    assert longest(["α", "β", "γγγ"]) == "γγγ"

def test_longest_with_unicode():
    assert longest(["🌟", "⭐⭐", "✨✨✨"]) == "✨✨✨"

def test_longest_multiple_same_length():
    result = longest(["abc", "def", "ghi"])
    assert len(result) == 3
    assert result in ["abc", "def", "ghi"]