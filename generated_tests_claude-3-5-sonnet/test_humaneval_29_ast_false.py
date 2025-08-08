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

@pytest.mark.parametrize("strings,prefix,expected", [
    (["apple", "banana", "apricot"], "a", ["apple", "apricot"]),
    (["cat", "dog", "fish"], "c", ["cat"]),
    ([], "x", []),
    (["test", "testing", "tested"], "test", ["test", "testing", "tested"]),
    (["hello", "world"], "", ["hello", "world"]),
    (["Python", "python", "PYTHON"], "py", ["python"]),
    (["a", "ab", "abc"], "abc", ["abc"]),
    (["prefix", "pre", "prefix"], "pre", ["prefix", "pre", "prefix"]),
    ([" space", "no space"], " ", [" space"]),
    (["special!@#", "special", "sp"], "special", ["special!@#", "special"]),
])
def test_filter_by_prefix_parametrized(strings: List[str], prefix: str, expected: List[str]):
    from filter_strings import filter_by_prefix
    assert filter_by_prefix(strings, prefix) == expected

def test_filter_by_prefix_empty_prefix():
    strings = ["a", "b", "c"]
    assert filter_by_prefix(strings, "") == strings

def test_filter_by_prefix_no_matches():
    strings = ["apple", "banana", "cherry"]
    assert filter_by_prefix(strings, "x") == []

def test_filter_by_prefix_case_sensitive():
    strings = ["Apple", "apple", "APPLE"]
    assert filter_by_prefix(strings, "app") == ["apple"]

@pytest.mark.parametrize("invalid_strings", [
    None,
    42,
    [1, 2, 3],
    [None],
    ["valid", None, "invalid"],
])
def test_filter_by_prefix_invalid_input(invalid_strings):
    with pytest.raises((TypeError, AttributeError)):
        filter_by_prefix(invalid_strings, "test")

@pytest.mark.parametrize("invalid_prefix", [
    None,
    42,
    ["not", "a", "string"],
    {"key": "value"},
])
def test_filter_by_prefix_invalid_prefix(invalid_prefix):
    with pytest.raises((TypeError, AttributeError)):
        filter_by_prefix(["test", "testing"], invalid_prefix)