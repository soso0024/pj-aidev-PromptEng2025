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

def filter_by_substring(strings: List[str], substring: str):
    return [x for x in strings if substring in x]

def test_filter_by_substring_normal_case():
    input_list = ['apple', 'banana', 'cherry']
    result = filter_by_substring(input_list, 'an')
    assert result == ['banana']

def test_filter_by_substring_multiple_matches():
    input_list = ['hello', 'world', 'hello world']
    result = filter_by_substring(input_list, 'hello')
    assert result == ['hello', 'hello world']

def test_filter_by_substring_no_matches():
    input_list = ['python', 'java', 'cpp']
    result = filter_by_substring(input_list, 'ruby')
    assert result == []

def test_filter_by_substring_empty_list():
    input_list = []
    result = filter_by_substring(input_list, 'test')
    assert result == []

def test_filter_by_substring_empty_substring():
    input_list = ['apple', 'banana', 'cherry']
    result = filter_by_substring(input_list, '')
    assert result == input_list

@pytest.mark.parametrize("input_list,substring,expected", [
    (['hello', 'world', 'hello world'], 'hello', ['hello', 'hello world']),
    (['python', 'java', 'cpp'], 'a', ['java']),
    ([], 'test', []),
    (['abc', 'def', 'ghi'], '', ['abc', 'def', 'ghi'])
])
def test_filter_by_substring_parametrized(input_list, substring, expected):
    assert filter_by_substring(input_list, substring) == expected

def test_filter_by_substring_case_sensitive():
    input_list = ['Hello', 'hello', 'HELLO']
    result = filter_by_substring(input_list, 'hello')
    assert result == ['hello']

def test_filter_by_substring_special_characters():
    input_list = ['a!b', 'c@d', 'e#f']
    result = filter_by_substring(input_list, '@')
    assert result == ['c@d']
