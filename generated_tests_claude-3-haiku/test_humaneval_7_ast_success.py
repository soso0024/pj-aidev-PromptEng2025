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
    assert filter_by_substring([], "test") == []

def test_filter_by_substring_single_match():
    assert filter_by_substring(["hello", "world", "test"], "test") == ["test"]

def test_filter_by_substring_multiple_matches():
    assert filter_by_substring(["hello", "test", "another test"], "test") == ["test", "another test"]

def test_filter_by_substring_no_matches():
    assert filter_by_substring(["hello", "world", "another"], "test") == []

@pytest.mark.parametrize("strings,substring,expected", [
    ([], "test", []),
    (["hello", "world", "test"], "test", ["test"]),
    (["hello", "test", "another test"], "test", ["test", "another test"]),
    (["hello", "world", "another"], "test", [])
])
def test_filter_by_substring_parametrized(strings, substring, expected):
    assert filter_by_substring(strings, substring) == expected

def filter_by_substring(strings: list[str], substring: str):
    return [x for x in strings if substring in x]
