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
    ("", []),
    ("a", ["a"]),
    ("abc", ["a", "ab", "abc"]),
    ("test", ["t", "te", "tes", "test"]),
    ("12345", ["1", "12", "123", "1234", "12345"]),
    (" ", [" "]),
    ("!@#", ["!", "!@", "!@#"]),
    ("Hello", ["H", "He", "Hel", "Hell", "Hello"]),
    ("  ", [" ", "  "]),
    ("a b", ["a", "a ", "a b"])
])
def test_all_prefixes_parametrized(input_str: str, expected: List[str]):
    assert all_prefixes(input_str) == expected

def test_all_prefixes_empty_string():
    assert all_prefixes("") == []

def test_all_prefixes_single_char():
    assert all_prefixes("x") == ["x"]

def test_all_prefixes_special_chars():
    assert all_prefixes("\n\t") == ["\n", "\n\t"]

def test_all_prefixes_unicode():
    assert all_prefixes("🌟") == ["🌟"]
    assert all_prefixes("é") == ["é"]

def test_all_prefixes_result_type():
    result = all_prefixes("test")
    assert isinstance(result, list)
    assert all(isinstance(x, str) for x in result)

def test_all_prefixes_preserves_whitespace():
    assert all_prefixes("a b c") == ["a", "a ", "a b", "a b ", "a b c"]

@pytest.mark.parametrize("input_str", [None, 123, ["a"], {"key": "value"}, 3.14])
def test_all_prefixes_invalid_input(input_str):
    with pytest.raises(TypeError):
        all_prefixes(input_str)