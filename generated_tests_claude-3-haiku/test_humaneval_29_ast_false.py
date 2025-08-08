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

def test_filter_by_prefix_empty_list():
    assert filter_by_prefix([], 'abc') == []

def test_filter_by_prefix_empty_prefix():
    assert filter_by_prefix(['apple', 'banana', 'cherry'], '') == ['apple', 'banana', 'cherry']

@pytest.mark.parametrize("strings,prefix,expected", [
    (['apple', 'banana', 'cherry'], 'a', ['apple']),
    (['apple', 'banana', 'cherry'], 'b', ['banana']),
    (['apple', 'banana', 'cherry'], 'c', ['cherry']),
    (['apple', 'banana', 'cherry'], 'x', []),
    (['apple', 'banana', 'cherry'], 'ap', ['apple']),
    (['apple', 'banana', 'cherry'], 'an', ['banana']),
    (['apple', 'banana', 'cherry'], 'ch', ['cherry'])
])
def test_filter_by_prefix_normal_cases(strings, prefix, expected):
    assert filter_by_prefix(strings, prefix) == expected

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]