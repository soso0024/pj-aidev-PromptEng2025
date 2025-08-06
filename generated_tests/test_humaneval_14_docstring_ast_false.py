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


@pytest.mark.parametrize("input_str,expected", [
    ("abc", ["a", "ab", "abc"]),
    ("a", ["a"]),
    ("", []),
    ("hello", ["h", "he", "hel", "hell", "hello"]),
    ("12345", ["1", "12", "123", "1234", "12345"]),
    (" ", [" "]),
    ("a b", ["a", "a ", "a b"]),
    ("!@#", ["!", "!@", "!@#"]),
])
def test_all_prefixes_various_inputs(input_str: str, expected: List[str]):
    assert all_prefixes(input_str) == expected


def test_all_prefixes_empty_string():
    assert all_prefixes("") == []


def test_all_prefixes_single_char():
    assert all_prefixes("x") == ["x"]


def test_all_prefixes_special_chars():
    assert all_prefixes("\n\t") == ["\n", "\n\t"]


def test_all_prefixes_unicode():
    assert all_prefixes("🌟✨") == ["🌟", "🌟✨"]


def test_all_prefixes_type():
    result = all_prefixes("test")
    assert isinstance(result, list)
    assert all(isinstance(x, str) for x in result)


def test_all_prefixes_preserves_whitespace():
    assert all_prefixes("  ") == [" ", "  "]


@pytest.mark.parametrize("invalid_input", [
    None,
    123,
    3.14
])
def test_all_prefixes_invalid_input(invalid_input):
    with pytest.raises((TypeError, AttributeError)):
        all_prefixes(invalid_input)


def test_all_prefixes_sequence_input():
    with pytest.raises((TypeError, AttributeError)):
        all_prefixes(["list"])
    with pytest.raises((TypeError, AttributeError)):
        all_prefixes({"dict": "value"})
    with pytest.raises((TypeError, AttributeError)):
        all_prefixes((1, 2, 3))