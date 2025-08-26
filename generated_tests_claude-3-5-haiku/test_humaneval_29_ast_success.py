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

def test_filter_by_prefix_normal_case():
    assert filter_by_prefix(['apple', 'banana', 'apricot'], 'a') == ['apple', 'apricot']

def test_filter_by_prefix_empty_list():
    assert filter_by_prefix([], 'test') == []

def test_filter_by_prefix_no_matches():
    assert filter_by_prefix(['hello', 'world'], 'x') == []

def test_filter_by_prefix_case_sensitive():
    assert filter_by_prefix(['Apple', 'apple', 'Apricot'], 'a') == ['apple']

@pytest.mark.parametrize("strings,prefix,expected", [
    (['hello', 'world', 'help'], 'he', ['hello', 'help']),
    (['python', 'pytest', 'java'], 'py', ['python', 'pytest']),
    (['', 'test', 'another'], '', ['', 'test', 'another'])
])
def test_filter_by_prefix_parametrized(strings, prefix, expected):
    assert filter_by_prefix(strings, prefix) == expected

def test_filter_by_prefix_unicode():
    assert filter_by_prefix(['café', 'cafè', 'coffee'], 'caf') == ['café', 'cafè']

def test_filter_by_prefix_whitespace():
    assert filter_by_prefix([' test', 'test', 'testing'], 'test') == ['test', 'testing']
