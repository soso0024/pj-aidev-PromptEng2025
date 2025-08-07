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

def test_filter_by_substring_normal_case():
    assert filter_by_substring(['apple', 'banana', 'cherry'], 'an') == ['banana']

def test_filter_by_substring_multiple_matches():
    assert filter_by_substring(['python', 'java', 'javascript'], 'java') == ['java', 'javascript']

def test_filter_by_substring_empty_list():
    assert filter_by_substring([], 'test') == []

def test_filter_by_substring_empty_substring():
    assert filter_by_substring(['hello', 'world'], '') == ['hello', 'world']

def test_filter_by_substring_case_sensitive():
    assert filter_by_substring(['Python', 'python', 'PYTHON'], 'python') == ['python']

@pytest.mark.parametrize("input_list,substring,expected", [
    (['hello', 'world', 'hello world'], 'hello', ['hello', 'hello world']),
    (['abc', 'def', 'ghi'], 'x', []),
    (['', 'test', ''], '', ['', '', 'test']),
    (['Python3.9', 'Python3.10', 'Java'], '3.', ['Python3.9', 'Python3.10'])
])
def test_filter_by_substring_parametrized(input_list, substring, expected):
    assert filter_by_substring(input_list, substring) == expected

def test_filter_by_substring_non_string_input():
    with pytest.raises(TypeError):
        filter_by_substring([1, 2, 3], 'test')

def test_filter_by_substring_none_input():
    with pytest.raises(TypeError):
        filter_by_substring(None, 'test')