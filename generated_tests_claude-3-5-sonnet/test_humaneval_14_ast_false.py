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
from all_prefixes import all_prefixes

@pytest.mark.parametrize("input_str,expected", [
    ("", [""]),
    ("a", ["a"]),
    ("ab", ["a", "ab"]),
    ("abc", ["a", "ab", "abc"]),
    ("test", ["t", "te", "tes", "test"]),
    ("hello", ["h", "he", "hel", "hell", "hello"]),
    ("12345", ["1", "12", "123", "1234", "12345"]),
    (" ", [" "]),
    ("a b", ["a", "a ", "a b"]),
    ("!@#", ["!", "!@", "!@#"]),
])
def test_all_prefixes_valid_inputs(input_str: str, expected: List[str]):
    assert all_prefixes(input_str) == expected

def test_all_prefixes_empty_string():
    assert all_prefixes("") == [""]

def test_all_prefixes_single_char():
    assert all_prefixes("x") == ["x"]

def test_all_prefixes_special_chars():
    assert all_prefixes("\n\t") == ["\n", "\n\t"]

def test_all_prefixes_unicode():
    assert all_prefixes("🐍") == ["🐍"]
    assert all_prefixes("🐍🐘") == ["🐍", "🐍🐘"]

@pytest.mark.parametrize("invalid_input", [
    None,
    123,
    ["list"],
    {"dict": "value"},
    (1, 2, 3),
    True,
    3.14
])
def test_all_prefixes_invalid_inputs(invalid_input):
    with pytest.raises((TypeError, AttributeError)):
        all_prefixes(invalid_input)

def test_all_prefixes_result_type():
    result = all_prefixes("test")
    assert isinstance(result, list)
    assert all(isinstance(x, str) for x in result)

def test_all_prefixes_preserves_whitespace():
    assert all_prefixes("  ") == [" ", "  "]

def test_all_prefixes_long_string():
    long_str = "x" * 1000
    result = all_prefixes(long_str)
    assert len(result) == 1000
    assert all(len(result[i]) == i + 1 for i in range(1000))