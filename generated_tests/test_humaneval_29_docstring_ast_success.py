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
    ([], "a", []),
    (["abc", "bcd", "cde", "array"], "a", ["abc", "array"]),
    (["abc", "bcd", "cde"], "b", ["bcd"]),
    (["abc", "bcd", "cde"], "d", []),
    (["", "abc", "bcd"], "", ["", "abc", "bcd"]),
    (["abc", "abc123", "abcdef"], "abc", ["abc", "abc123", "abcdef"]),
    (["ABC", "abc"], "a", ["abc"]),
    (["123", "456", "789"], "1", ["123"]),
    ([" abc", " def"], " ", [" abc", " def"]),
])
def test_filter_by_prefix(strings, prefix, expected):
    assert filter_by_prefix(strings, prefix) == expected


def test_filter_by_prefix_with_none():
    with pytest.raises(AttributeError):
        filter_by_prefix(["abc", "def", None], "a")


def test_filter_by_prefix_type_error():
    with pytest.raises(TypeError):
        filter_by_prefix(None, "a")
    with pytest.raises(AttributeError):
        filter_by_prefix([1, 2, 3], "a")
    with pytest.raises(TypeError):
        filter_by_prefix(["abc"], None)


def test_filter_by_prefix_empty_prefix():
    assert filter_by_prefix(["abc", "def"], "") == ["abc", "def"]


def test_filter_by_prefix_case_sensitive():
    assert filter_by_prefix(["ABC", "abc", "Abc"], "a") == ["abc"]
    assert filter_by_prefix(["ABC", "abc", "Abc"], "A") == ["ABC", "Abc"]


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]