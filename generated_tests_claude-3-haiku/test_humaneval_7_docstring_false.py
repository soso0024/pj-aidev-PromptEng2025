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
from typing import List
import pytest

def test_filter_by_substring_empty_list():
    assert filter_by_substring([], 'a') == []

def test_filter_by_substring_normal_case():
    assert filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a') == ['abc', 'bacd', 'array']

def test_filter_by_substring_no_match():
    assert filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'x') == []

def test_filter_by_substring_single_element_list():
    assert filter_by_substring(['abc'], 'a') == ['abc']

def test_filter_by_substring_case_insensitive():
    assert filter_by_substring(['Abc', 'baCD', 'cde', 'Array'], 'a') == ['Abc', 'baCD', 'Array']

@pytest.mark.parametrize("strings,substring,expected", [
    ([], 'a', []),
    (['abc', 'bacd', 'cde', 'array'], 'a', ['abc', 'bacd', 'array']),
    (['abc', 'bacd', 'cde', 'array'], 'x', []),
    (['abc'], 'a', ['abc']),
    (['Abc', 'baCD', 'cde', 'Array'], 'a', ['Abc', 'baCD', 'Array'])
])
def test_filter_by_substring_parametrized(strings, substring, expected):
    assert filter_by_substring(strings, substring) == expected