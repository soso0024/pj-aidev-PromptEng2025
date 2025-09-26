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
    assert filter_by_prefix([], 'test') == []

def test_filter_by_prefix_no_matches():
    assert filter_by_prefix(['apple', 'banana', 'cherry'], 'test') == []

def test_filter_by_prefix_single_match():
    assert filter_by_prefix(['test', 'apple', 'testcase'], 'test') == ['test', 'testcase']

def test_filter_by_prefix_multiple_matches():
    assert filter_by_prefix(['hello', 'test', 'world', 'testing'], 'test') == ['test', 'testing']

def test_filter_by_prefix_case_sensitive():
    assert filter_by_prefix(['Test', 'test', 'TEST'], 'test') == ['test']

@pytest.mark.parametrize("strings,prefix,expected", [
    ([], 'test', []),
    (['apple', 'banana', 'cherry'], 'test', []),
    (['test', 'apple', 'testcase'], 'test', ['test', 'testcase']),
    (['hello', 'test', 'world', 'testing'], 'test', ['test', 'testing']),
    (['Test', 'test', 'TEST'], 'test', ['test'])
])
def test_filter_by_prefix_parametrized(strings, prefix, expected):
    assert filter_by_prefix(strings, prefix) == expected

def filter_by_prefix(strings: list[str], prefix: str):
    return [x for x in strings if x.startswith(prefix)]
