# Test cases for HumanEval/29
# Generated using Claude API

from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.
    >>> filter_by_prefix([], 'a')
    []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    """

    return [x for x in strings if x.startswith(prefix)]


# Generated test cases:
import pytest
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]


def test_empty_list():
    assert filter_by_prefix([], 'a') == []


def test_empty_prefix():
    assert filter_by_prefix(['abc', 'def', 'ghi'], '') == ['abc', 'def', 'ghi']


def test_no_matches():
    assert filter_by_prefix(['xyz', 'uvw', 'rst'], 'a') == []


def test_all_matches():
    assert filter_by_prefix(['apple', 'apricot', 'avocado'], 'a') == ['apple', 'apricot', 'avocado']


def test_some_matches():
    assert filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a') == ['abc', 'array']


def test_single_character_strings():
    assert filter_by_prefix(['a', 'b', 'c', 'a'], 'a') == ['a', 'a']


def test_prefix_longer_than_strings():
    assert filter_by_prefix(['a', 'ab', 'abc'], 'abcd') == []


def test_exact_match():
    assert filter_by_prefix(['hello', 'world'], 'hello') == ['hello']


def test_case_sensitive():
    assert filter_by_prefix(['Apple', 'apple', 'APPLE'], 'a') == ['apple']


def test_special_characters():
    assert filter_by_prefix(['@test', '#test', '@hello'], '@') == ['@test', '@hello']


def test_numbers_as_strings():
    assert filter_by_prefix(['123', '456', '12abc'], '12') == ['123', '12abc']


def test_whitespace_prefix():
    assert filter_by_prefix([' hello', 'hello', ' world'], ' ') == [' hello', ' world']


def test_unicode_characters():
    assert filter_by_prefix(['café', 'car', 'cañon'], 'ca') == ['café', 'car', 'cañon']


@pytest.mark.parametrize("strings,prefix,expected", [
    ([], 'test', []),
    (['hello'], 'h', ['hello']),
    (['hello'], 'x', []),
    (['a', 'aa', 'aaa'], 'aa', ['aa', 'aaa']),
    (['test123', 'test456', 'other'], 'test', ['test123', 'test456'])
])
def test_parametrized_cases(strings, prefix, expected):
    assert filter_by_prefix(strings, prefix) == expected
