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

@pytest.mark.parametrize("strings,expected", [
    ([], None),
    (['abc', 'def', 'ghi'], 'abc'),
    (['short', 'longer', 'longest'], 'longest'),
    (['one', 'two', 'three'], 'three'),
    (['a', 'bb', 'ccc'], 'ccc'),
    ([' ', '  ', '   '], '   '),
    ([''], None),
])
def test_longest(strings: List[str], expected: Optional[str]):
    assert longest(strings) == expected

def test_longest_empty_list():
    assert longest([]) is None

def test_longest_single_element():
    assert longest(['abc']) == 'abc'

def test_longest_multiple_max_length():
    assert longest(['aaa', 'bbb', 'ccc']) in ['aaa', 'bbb', 'ccc']

def test_longest_all_same_length():
    assert longest(['abc', 'def', 'ghi']) == 'abc'