# Test cases for HumanEval/7
# Generated using Claude API

from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    """

    return [x for x in strings if substring in x]


# Generated test cases:
import pytest

def test_filter_by_substring_empty_list():
    assert filter_by_substring([], 'a') == []

def test_filter_by_substring_normal_case():
    assert filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a') == ['abc', 'bacd', 'array']

def test_filter_by_substring_case_sensitive():
    assert filter_by_substring(['ABC', 'abc', 'def'], 'a') == ['abc']

def test_filter_by_substring_no_matches():
    assert filter_by_substring(['xyz', 'pqr', 'mno'], 'a') == []

def test_filter_by_substring_full_match():
    assert filter_by_substring(['hello', 'world', 'hello world'], 'hello world') == ['hello world']

def test_filter_by_substring_empty_substring():
    assert filter_by_substring(['abc', 'def', 'ghi'], '') == ['abc', 'def', 'ghi']

@pytest.mark.parametrize("input_list,substring,expected", [
    ([], 'a', []),
    (['abc', 'bacd', 'cde', 'array'], 'a', ['abc', 'bacd', 'array']),
    (['ABC', 'abc', 'def'], 'a', ['abc']),
    (['xyz', 'pqr', 'mno'], 'a', []),
    (['hello', 'world', 'hello world'], 'hello world', ['hello world']),
    (['abc', 'def', 'ghi'], '', ['abc', 'def', 'ghi'])
])
def test_filter_by_substring_parametrized(input_list, substring, expected):
    assert filter_by_substring(input_list, substring) == expected
