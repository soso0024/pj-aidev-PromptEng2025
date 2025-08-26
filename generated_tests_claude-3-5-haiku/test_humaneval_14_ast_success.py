# Test cases for HumanEval/14
# Generated using Claude API

from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """

    result = []

    for i in range(len(string)):
        result.append(string[:i+1])
    return result


# Generated test cases:
import pytest

def test_all_prefixes_empty_string():
    assert all_prefixes("") == []

def test_all_prefixes_single_char():
    assert all_prefixes("a") == ["a"]

def test_all_prefixes_multiple_chars():
    assert all_prefixes("hello") == ["h", "he", "hel", "hell", "hello"]

def test_all_prefixes_unicode_string():
    assert all_prefixes("café") == ["c", "ca", "caf", "café"]

@pytest.mark.parametrize("input_string,expected", [
    ("", []),
    ("a", ["a"]),
    ("hello", ["h", "he", "hel", "hell", "hello"]),
    ("python", ["p", "py", "pyt", "pyth", "pytho", "python"])
])
def test_all_prefixes_parametrized(input_string, expected):
    assert all_prefixes(input_string) == expected

def test_all_prefixes_numeric_string():
    assert all_prefixes("123") == ["1", "12", "123"]

def test_all_prefixes_mixed_chars():
    assert all_prefixes("a1b2") == ["a", "a1", "a1b", "a1b2"]
