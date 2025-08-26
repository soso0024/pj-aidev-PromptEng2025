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

def filter_by_prefix(strings: List[str], prefix: str):
    return [x for x in strings if x.startswith(prefix)]

def test_filter_by_prefix_basic():
    assert filter_by_prefix(['apple', 'banana', 'apricot'], 'a') == ['apple', 'apricot']

def test_filter_by_prefix_empty_list():
    assert filter_by_prefix([], 'test') == []

def test_filter_by_prefix_no_matches():
    assert filter_by_prefix(['hello', 'world'], 'x') == []

def test_filter_by_prefix_case_sensitive():
    assert filter_by_prefix(['Apple', 'apple', 'Apricot'], 'a') == ['apple']

def test_filter_by_prefix_empty_prefix():
    assert filter_by_prefix(['test', 'testing', 'other'], '') == ['test', 'testing', 'other']

@pytest.mark.parametrize("input_list,prefix,expected", [
    (['hello', 'world', 'help'], 'he', ['hello', 'help']),
    (['python', 'pytest', 'java'], 'py', ['python', 'pytest']),
    (['', 'abc', 'def'], '', ['', 'abc', 'def']),
    ([], 'test', [])
])
def test_filter_by_prefix_parametrized(input_list, prefix, expected):
    assert filter_by_prefix(input_list, prefix) == expected

def test_filter_by_prefix_unicode():
    assert filter_by_prefix(['café', 'cafè', 'coffee'], 'caf') == ['café', 'cafè']

def test_filter_by_prefix_numeric_strings():
    assert filter_by_prefix(['123', '456', '12345'], '12') == ['123', '12345']
