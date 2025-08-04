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
from filter_by_prefix import filter_by_prefix

@pytest.mark.parametrize("strings, prefix, expected", [
    (["apple", "banana", "apricot"], "a", ["apple", "apricot"]),
    (["cat", "dog", "fish"], "d", ["dog"]),
    ([], "x", []),
    (["test"], "", ["test"]),
    (["hello", "help", "held"], "hel", ["hello", "help", "held"]),
    (["abc", "def", "ghi"], "xyz", []),
    (["A", "a", "ABC", "abc"], "a", ["a", "abc"]),
    (["test", "testing", "tested"], "test", ["test", "testing", "tested"]),
    ([" space", "no space"], " ", [" space"]),
    (["one", "two", "three"], "four", []),
])
def test_filter_by_prefix_parametrized(strings: List[str], prefix: str, expected: List[str]):
    assert filter_by_prefix(strings, prefix) == expected

def test_filter_by_prefix_empty_prefix():
    strings = ["a", "b", "c"]
    assert filter_by_prefix(strings, "") == strings

def test_filter_by_prefix_case_sensitivity():
    strings = ["Test", "test", "TEST"]
    assert filter_by_prefix(strings, "test") == ["test"]
    assert filter_by_prefix(strings, "Test") == ["Test"]

def test_filter_by_prefix_special_characters():
    strings = ["@test", "#test", "$test"]
    assert filter_by_prefix(strings, "@") == ["@test"]
    assert filter_by_prefix(strings, "#") == ["#test"]

def test_filter_by_prefix_with_spaces():
    strings = ["  leading", "trailing  ", "no spaces"]
    assert filter_by_prefix(strings, "  ") == ["  leading"]

@pytest.mark.parametrize("invalid_strings", [
    None,
    42,
    True,
    {"set", "of", "strings"}
])
def test_filter_by_prefix_invalid_input_type(invalid_strings):
    with pytest.raises((TypeError, AttributeError)):
        filter_by_prefix(invalid_strings, "test")

@pytest.mark.parametrize("invalid_prefix", [
    None,
    42,
    True,
    ["list"],
    {"dict": "value"},
])
def test_filter_by_prefix_invalid_prefix_type(invalid_prefix):
    with pytest.raises((TypeError, AttributeError)):
        filter_by_prefix(["test"], invalid_prefix)