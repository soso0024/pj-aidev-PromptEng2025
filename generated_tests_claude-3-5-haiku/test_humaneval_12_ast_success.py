# Test cases for HumanEval/12
# Generated using Claude API

from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    >>> longest([])

    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    """

    if not strings:
        return None

    maxlen = max(len(x) for x in strings)
    for s in strings:
        if len(s) == maxlen:
            return s


# Generated test cases:
import pytest
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None

    maxlen = max(len(x) for x in strings)
    for s in strings:
        if len(s) == maxlen:
            return s

def test_longest_normal_cases():
    assert longest(["a", "ab", "abc"]) == "abc"
    assert longest(["python", "java", "c++"]) == "python"
    assert longest(["short", "longer", "longest"]) == "longest"

def test_longest_multiple_max_length():
    assert longest(["hello", "world"]) in ["hello", "world"]

def test_longest_empty_list():
    assert longest([]) is None

def test_longest_single_element():
    assert longest(["single"]) == "single"

def test_longest_equal_length_strings():
    result = longest(["cat", "dog", "rat"])
    assert result in ["cat", "dog", "rat"]

def test_longest_with_special_characters():
    assert longest(["a!", "b@", "c#"]) in ["a!", "b@", "c#"]

def test_longest_with_unicode():
    assert longest(["café", "naïve", "résumé"]) == "résumé"

def test_longest_mixed_case():
    assert longest(["SHORT", "LONGER", "LONGEST"]) == "LONGEST"

def test_longest_whitespace():
    assert longest(["", " ", "  "]) == "  "

@pytest.mark.parametrize("input_list,expected", [
    (["a", "ab", "abc"], "abc"),
    (["python", "java", "c++"], "python"),
    (["hello", "world"], ["hello", "world"]),
    ([], None),
    (["single"], "single"),
    (["a!", "b@", "c#"], ["a!", "b@", "c#"]),
    (["café", "naïve", "résumé"], "résumé")
])
def test_longest_parametrized(input_list, expected):
    result = longest(input_list)
    if isinstance(expected, list):
        assert result in expected
    else:
        assert result == expected
