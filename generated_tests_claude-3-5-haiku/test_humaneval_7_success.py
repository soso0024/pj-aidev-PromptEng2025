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

def test_filter_by_substring_basic():
    input_list = ['apple', 'banana', 'cherry']
    result = filter_by_substring(input_list, 'an')
    assert result == ['banana']

def test_filter_by_substring_multiple_matches():
    input_list = ['hello', 'world', 'hello world']
    result = filter_by_substring(input_list, 'hello')
    assert result == ['hello', 'hello world']

def test_filter_by_substring_empty_list():
    input_list = []
    result = filter_by_substring(input_list, 'test')
    assert result == []

def test_filter_by_substring_no_matches():
    input_list = ['python', 'pytest', 'testing']
    result = filter_by_substring(input_list, 'xyz')
    assert result == []

def test_filter_by_substring_case_sensitive():
    input_list = ['Python', 'python', 'PYTHON']
    result = filter_by_substring(input_list, 'python')
    assert result == ['python']

@pytest.mark.parametrize("input_list,substring,expected", [
    (['hello', 'world', 'hello world'], 'hello', ['hello', 'hello world']),
    (['apple', 'banana', 'cherry'], 'an', ['banana']),
    ([], 'test', []),
    (['Python', 'python', 'PYTHON'], 'python', ['python'])
])
def test_filter_by_substring_parametrized(input_list, substring, expected):
    assert filter_by_substring(input_list, substring) == expected

def test_filter_by_substring_empty_substring():
    input_list = ['hello', 'world']
    result = filter_by_substring(input_list, '')
    assert result == input_list

def test_filter_by_substring_non_string_input():
    with pytest.raises(TypeError):
        filter_by_substring([1, 2, 3], 'test')
