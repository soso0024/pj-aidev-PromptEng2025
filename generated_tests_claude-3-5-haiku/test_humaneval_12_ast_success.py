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

def test_longest_normal_cases():
    assert longest(["a", "ab", "abc"]) == "abc"
    assert longest(["python", "java", "c++"]) == "python"
    assert longest(["short", "longer", "longest"]) == "longest"

def test_longest_equal_length():
    assert longest(["cat", "dog", "rat"]) in ["cat", "dog", "rat"]

def test_longest_empty_list():
    assert longest([]) is None

def test_longest_single_element():
    assert longest(["hello"]) == "hello"

def test_longest_unicode_strings():
    assert longest(["café", "naïve", "résumé"]) == "résumé"

def test_longest_whitespace_strings():
    assert longest(["", "  ", "   "]) == "   "

@pytest.mark.parametrize("input_list,expected", [
    (["a", "ab", "abc"], "abc"),
    (["python", "java", "c++"], "python"),
    (["cat", "dog", "rat"], "cat"),
    ([""], ""),
    (["hello"], "hello"),
    (["café", "naïve", "résumé"], "résumé")
])
def test_longest_parametrized(input_list, expected):
    assert longest(input_list) == expected