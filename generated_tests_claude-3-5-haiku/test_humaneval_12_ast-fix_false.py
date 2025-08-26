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
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None

    maxlen = max(len(x) for x in strings)
    for s in strings:
        if len(s) == maxlen:
            return s

def test_longest_empty_list():
    assert longest([]) is None

def test_longest_single_string():
    assert longest(["hello"]) == "hello"

def test_longest_multiple_strings():
    assert longest(["a", "bb", "ccc"]) == "ccc"

def test_longest_multiple_equal_length_strings():
    assert longest(["cat", "dog", "rat"]) in ["cat", "dog", "rat"]

def test_longest_with_empty_strings():
    assert longest(["", "a", ""]) == "a"

def test_longest_unicode_strings():
    assert longest(["hello", "世界", "python"]) == "世界"

def test_longest_parametrized_1():
    assert longest(["short", "longer", "longest"]) == "longest"

def test_longest_parametrized_2():
    assert longest(["a", "ab", "abc", "abcd"]) == "abcd"

def test_longest_parametrized_3():
    assert longest(["", "", "x"]) == "x"

def test_longest_parametrized_4():
    assert longest(["equal", "equal"]) == "equal"