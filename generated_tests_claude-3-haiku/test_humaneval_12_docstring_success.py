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

def test_longest_single_element():
    assert longest(['a']) == 'a'

def test_longest_multiple_elements():
    assert longest(['a', 'bb', 'ccc']) == 'ccc'

def test_longest_multiple_longest_elements():
    assert longest(['aaa', 'bbb', 'ccc']) == 'aaa'

@pytest.mark.parametrize("input_list,expected", [
    ([], None),
    (['a'], 'a'),
    (['a', 'bb', 'ccc'], 'ccc'),
    (['aaa', 'bbb', 'ccc'], 'aaa')
])
def test_longest_parametrized(input_list, expected):
    assert longest(input_list) == expected
