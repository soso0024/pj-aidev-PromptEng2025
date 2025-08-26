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

def test_filter_by_prefix_no_matches():
    assert filter_by_prefix(['bcd', 'cde'], 'a') == []

def test_filter_by_prefix_some_matches():
    assert filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a') == ['abc', 'array']

def test_filter_by_prefix_case_sensitive():
    assert filter_by_prefix(['Abc', 'abc', 'bcd'], 'a') == ['abc']

def test_filter_by_prefix_empty_prefix():
    assert filter_by_prefix(['abc', 'def', 'ghi'], '') == ['abc', 'def', 'ghi']

@pytest.mark.parametrize("strings,prefix,expected", [
    ([], 'a', []),
    (['abc', 'bcd', 'cde', 'array'], 'a', ['abc', 'array']),
    (['hello', 'world', 'help'], 'he', ['hello', 'help']),
    (['Python', 'pytest', 'programming'], 'p', []),
    (['Python', 'pytest', 'programming'], 'P', ['Python'])
])
def test_filter_by_prefix_parametrized(strings, prefix, expected):
    assert filter_by_prefix(strings, prefix) == expected

def test_filter_by_prefix_unicode():
    assert filter_by_prefix(['café', 'cafè', 'hello'], 'caf') == ['café', 'cafè']