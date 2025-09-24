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
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

def test_filter_by_substring_empty_list():
    assert filter_by_substring([], 'a') == []

def test_filter_by_substring_normal_case():
    assert filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a') == ['abc', 'bacd', 'array']

def test_filter_by_substring_no_matches():
    assert filter_by_substring(['xyz', 'pqr', 'def'], 'a') == []

def test_filter_by_substring_single_element_list():
    assert filter_by_substring(['hello'], 'e') == ['hello']

@pytest.mark.parametrize("strings, substring, expected", [
    ([], 'a', []),
    (['abc', 'bacd', 'cde', 'array'], 'a', ['abc', 'bacd', 'array']),
    (['xyz', 'pqr', 'def'], 'a', []),
    (['hello'], 'e', ['hello'])
])
def test_filter_by_substring_parametrized(strings, substring, expected):
    assert filter_by_substring(strings, substring) == expected
