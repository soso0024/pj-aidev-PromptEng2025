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

def test_longest_normal_case():
    assert longest(["short", "longer", "longest"]) == "longest"

def test_longest_multiple_same_length():
    assert longest(["abc", "def", "ghi"]) == "abc"

def test_longest_empty_list():
    assert longest([]) is None

def test_longest_single_string():
    assert longest(["hello"]) == "hello"

def test_longest_with_empty_strings():
    assert longest(["", "a", ""]) == "a"

@pytest.mark.parametrize("input_list,expected", [
    (["python", "java", "javascript"], "javascript"),
    (["a", "bb", "ccc"], "ccc"),
    (["short", "medium", "longest"], "longest"),
    (["equal", "equal"], "equal"),
])
def test_longest_parametrized(input_list, expected):
    assert longest(input_list) == expected

def test_longest_unicode_strings():
    assert longest(["café", "naïve", "résumé"]) == "résumé"

def test_longest_mixed_length_strings():
    assert longest(["a", "bb", "c", "dddd", "eee"]) == "dddd"