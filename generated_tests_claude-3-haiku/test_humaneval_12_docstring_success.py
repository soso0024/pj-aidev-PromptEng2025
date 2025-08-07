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

def test_longest_empty_list():
    assert longest([]) is None

def test_longest_single_string():
    assert longest(['a']) == 'a'

def test_longest_multiple_strings():
    assert longest(['a', 'bb', 'ccc']) == 'ccc'

def test_longest_multiple_equal_length_strings():
    assert longest(['abc', 'def', 'ghi']) == 'abc'

@pytest.mark.parametrize("input_strings,expected", [
    ([], None),
    (['a'], 'a'),
    (['a', 'bb', 'ccc'], 'ccc'),
    (['abc', 'def', 'ghi'], 'abc')
])
def test_longest_parametrized(input_strings, expected):
    assert longest(input_strings) == expected
