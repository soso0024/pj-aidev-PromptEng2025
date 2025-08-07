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
    assert filter_by_substring([], 'test') == []

def test_filter_by_substring_empty_substring():
    assert filter_by_substring(['apple', 'banana', 'cherry'], '') == ['apple', 'banana', 'cherry']

@pytest.mark.parametrize("strings,substring,expected", [
    (['apple', 'banana', 'cherry'], 'a', ['apple', 'banana']),
    (['apple', 'banana', 'cherry'], 'r', ['cherry']),
    (['apple', 'banana', 'cherry'], 'x', [])
])
def test_filter_by_substring_normal_cases(strings, substring, expected):
    assert filter_by_substring(strings, substring) == expected

def test_filter_by_substring_type_error():
    with pytest.raises(TypeError):
        filter_by_substring(123, 'test')

def test_filter_by_substring_substring_not_str():
    with pytest.raises(TypeError):
        filter_by_substring(['apple', 'banana', 'cherry'], 123)

def filter_by_substring(strings: list[str], substring: str) -> list[str]:
    return [x for x in strings if substring in x]
