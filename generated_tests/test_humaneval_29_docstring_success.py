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


def test_empty_list():
    assert filter_by_prefix([], 'a') == []


def test_empty_prefix():
    assert filter_by_prefix(['abc', 'def'], '') == ['abc', 'def']


def test_no_matches():
    assert filter_by_prefix(['bcd', 'def', 'ghi'], 'a') == []


def test_single_match():
    assert filter_by_prefix(['abc', 'def', 'ghi'], 'a') == ['abc']


def test_multiple_matches():
    assert filter_by_prefix(['abc', 'adef', 'ghi', 'axy'], 'a') == ['abc', 'adef', 'axy']


def test_case_sensitive():
    assert filter_by_prefix(['Abc', 'abc'], 'a') == ['abc']


@pytest.mark.parametrize("strings, prefix, expected", [
    (["abc", "def"], "a", ["abc"]),
    (["abc", "abcd", "bcd"], "ab", ["abc", "abcd"]),
    (["", "abc"], "", ["", "abc"]),
    (["abc", "def"], "x", []),
    (["ABC", "abc"], "a", ["abc"]),
    (["abc", "abd", "abf", "bcd"], "ab", ["abc", "abd", "abf"]),
])
def test_filter_by_prefix_parametrized(strings, prefix, expected):
    assert filter_by_prefix(strings, prefix) == expected


def test_special_characters():
    assert filter_by_prefix(['#abc', '#def', 'ghi'], '#') == ['#abc', '#def']


def test_whitespace_prefix():
    assert filter_by_prefix(['  abc', ' def', 'ghi'], ' ') == ['  abc', ' def']


def test_unicode_strings():
    assert filter_by_prefix(['über', 'unter', 'über'], 'ü') == ['über', 'über']


@pytest.mark.parametrize("invalid_input", [
    None,
    42,
    True,
    3.14
])
def test_invalid_prefix_type(invalid_input):
    with pytest.raises(TypeError):
        filter_by_prefix(['abc'], invalid_input)


def test_none_in_list():
    with pytest.raises(AttributeError):
        filter_by_prefix([None, 'abc'], 'a')


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]