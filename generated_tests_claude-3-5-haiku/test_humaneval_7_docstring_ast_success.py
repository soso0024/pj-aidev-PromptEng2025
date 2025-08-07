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

def test_filter_by_substring_no_matches():
    assert filter_by_substring(['bcd', 'cde', 'efg'], 'x') == []

def test_filter_by_substring_case_sensitive():
    assert filter_by_substring(['ABC', 'abc', 'Abc'], 'a') == ['abc']

def test_filter_by_substring_full_match():
    assert filter_by_substring(['hello', 'world', 'hello world'], 'hello world') == ['hello world']

def test_filter_by_substring_multiple_occurrences():
    assert filter_by_substring(['banana', 'apple', 'ananas'], 'ana') == ['banana', 'ananas']

@pytest.mark.parametrize("input_list,substring,expected", [
    ([], 'test', []),
    (['hello', 'world'], 'o', ['hello', 'world']),
    (['python', 'java', 'cpp'], 'a', ['java']),
    (['', 'a', 'b'], '', ['', 'a', 'b'])
])
def test_filter_by_substring_parametrized(input_list, substring, expected):
    assert filter_by_substring(input_list, substring) == expected
