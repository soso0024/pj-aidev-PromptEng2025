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

def test_filter_by_prefix_empty_list():
    assert filter_by_prefix([], 'a') == []

def test_filter_by_prefix_normal_case():
    assert filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a') == ['abc', 'array']

def test_filter_by_prefix_no_matches():
    assert filter_by_prefix(['dog', 'cat', 'bird'], 'x') == []

def test_filter_by_prefix_case_sensitive():
    assert filter_by_prefix(['Apple', 'apple', 'Banana'], 'a') == ['apple']

def test_filter_by_prefix_empty_prefix():
    assert filter_by_prefix(['hello', 'world', ''], '') == ['hello', 'world', '']

@pytest.mark.parametrize("strings,prefix,expected", [
    ([], 'test', []),
    (['test1', 'test2', 'other'], 'test', ['test1', 'test2']),
    (['hello', 'world'], 'h', ['hello']),
    (['Python', 'pytest', 'programming'], 'p', ['Python', 'programming'])
])
def test_filter_by_prefix_parametrized(strings, prefix, expected):
    assert filter_by_prefix(strings, prefix) == expected