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

def test_filter_by_substring_basic():
    assert filter_by_substring(['hello', 'world', 'python'], 'o') == ['hello', 'world']

def test_filter_by_substring_empty_list():
    assert filter_by_substring([], 'test') == []

def test_filter_by_substring_no_matches():
    assert filter_by_substring(['apple', 'banana', 'cherry'], 'z') == []

def test_filter_by_substring_case_sensitive():
    assert filter_by_substring(['Hello', 'hello', 'HELLO'], 'hello') == ['hello']

@pytest.mark.parametrize("input_list,substring,expected", [
    (['test', 'testing', 'tester'], 'test', ['test', 'testing', 'tester']),
    (['abc', 'def', 'ghi'], '', ['abc', 'def', 'ghi']),
    (['python', 'java', 'javascript'], 'script', ['javascript'])
])
def test_filter_by_substring_parametrized(input_list, substring, expected):
    assert filter_by_substring(input_list, substring) == expected

def test_filter_by_substring_unicode():
    assert filter_by_substring(['café', 'naïve', 'résumé'], 'é') == ['café', 'naïve', 'résumé']

def test_filter_by_substring_whitespace():
    assert filter_by_substring(['hello world', 'hello  world', ' hello'], ' ') == ['hello world', 'hello  world', ' hello']