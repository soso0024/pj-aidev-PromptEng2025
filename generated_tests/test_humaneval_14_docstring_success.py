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
from typing import List


def test_basic_string():
    assert all_prefixes("abc") == ["a", "ab", "abc"]


def test_empty_string():
    assert all_prefixes("") == []


def test_single_character():
    assert all_prefixes("a") == ["a"]


@pytest.mark.parametrize("input_str,expected", [
    ("hello", ["h", "he", "hel", "hell", "hello"]),
    ("12345", ["1", "12", "123", "1234", "12345"]),
    ("a b", ["a", "a ", "a b"]),
    ("   ", [" ", "  ", "   "]),
])
def test_various_strings(input_str, expected):
    assert all_prefixes(input_str) == expected


def test_special_characters():
    assert all_prefixes("!@#") == ["!", "!@", "!@#"]


def test_with_numbers_and_letters():
    assert all_prefixes("ab12") == ["a", "ab", "ab1", "ab12"]


def test_with_unicode():
    assert all_prefixes("üñ") == ["ü", "üñ"]


def test_with_spaces():
    assert all_prefixes("a b c") == ["a", "a ", "a b", "a b ", "a b c"]


@pytest.mark.parametrize("input_str", [None, 123, 3.14])
def test_invalid_input_type(input_str):
    with pytest.raises(TypeError):
        all_prefixes(input_str)


def test_invalid_list_input():
    with pytest.raises(TypeError):
        all_prefixes([])


def test_invalid_dict_input():
    with pytest.raises(TypeError):
        all_prefixes({})


def all_prefixes(string: str) -> List[str]:
    if not isinstance(string, str):
        raise TypeError("Input must be a string")
    result = []
    for i in range(len(string)):
        result.append(string[:i+1])
    return result