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
    assert longest(['hello']) == 'hello'

def test_longest_multiple_strings():
    assert longest(['apple', 'banana', 'cherry']) == 'banana'

def test_longest_strings_with_same_length():
    assert longest(['foo', 'bar', 'baz']) in ['foo', 'bar', 'baz']

@pytest.mark.parametrize("input,expected", [
    ([], None),
    (['hello'], 'hello'),
    (['apple', 'banana', 'cherry'], 'banana'),
    (['foo', 'bar', 'baz'], ['foo', 'bar', 'baz'])
])
def test_longest_with_parametrize(input, expected):
    result = longest(input)
    if isinstance(expected, list):
        assert result in expected
    else:
        assert result == expected
