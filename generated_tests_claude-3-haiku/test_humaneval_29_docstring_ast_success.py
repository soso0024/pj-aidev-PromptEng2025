# Test cases for HumanEval/29
# Generated using Claude API

from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.
    >>> filter_by_prefix([], 'a')
    []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    """

    return [x for x in strings if x.startswith(prefix)]


# Generated test cases:
import pytest
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]

def test_filter_by_prefix_empty_list():
    assert filter_by_prefix([], 'a') == []

def test_filter_by_prefix_single_match():
    assert filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a') == ['abc', 'array']

def test_filter_by_prefix_no_matches():
    assert filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'x') == []

def test_filter_by_prefix_all_match():
    assert filter_by_prefix(['apple', 'ape', 'ant'], 'a') == ['apple', 'ape', 'ant']

@pytest.mark.parametrize("strings,prefix,expected", [
    ([], 'a', []),
    (['abc', 'bcd', 'cde', 'array'], 'a', ['abc', 'array']),
    (['abc', 'bcd', 'cde', 'array'], 'x', []),
    (['apple', 'ape', 'ant'], 'a', ['apple', 'ape', 'ant'])
])
def test_filter_by_prefix_parametrized(strings, prefix, expected):
    assert filter_by_prefix(strings, prefix) == expected
