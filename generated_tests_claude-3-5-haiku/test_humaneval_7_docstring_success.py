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

def test_empty_list():
    assert filter_by_substring([], 'a') == []

def test_no_matches():
    assert filter_by_substring(['bcd', 'efg'], 'a') == []

def test_some_matches():
    assert filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a') == ['abc', 'bacd', 'array']

def test_case_sensitive():
    assert filter_by_substring(['ABC', 'abc', 'def'], 'a') == ['abc']

def test_substring_at_start():
    assert filter_by_substring(['apple', 'banana', 'cherry'], 'app') == ['apple']

def test_substring_at_end():
    assert filter_by_substring(['grape', 'orange', 'pine'], 'ine') == ['pine']

def test_full_match():
    assert filter_by_substring(['hello', 'world'], 'hello') == ['hello']

@pytest.mark.parametrize("input_list,substring,expected", [
    ([], 'test', []),
    (['hello', 'world'], 'o', ['hello', 'world']),
    (['python', 'java', 'cpp'], 'a', ['java']),
    (['', 'abc', 'def'], '', ['', 'abc', 'def'])
])
def test_parametrized_cases(input_list, substring, expected):
    assert filter_by_substring(input_list, substring) == expected
