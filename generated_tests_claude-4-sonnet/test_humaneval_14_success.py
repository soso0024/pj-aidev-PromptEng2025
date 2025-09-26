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

def all_prefixes(string: str):
    result = []
    for i in range(len(string)):
        result.append(string[:i+1])
    return result

def test_empty_string():
    assert all_prefixes("") == []

def test_single_character():
    assert all_prefixes("a") == ["a"]

def test_two_characters():
    assert all_prefixes("ab") == ["a", "ab"]

def test_normal_string():
    assert all_prefixes("hello") == ["h", "he", "hel", "hell", "hello"]

def test_string_with_spaces():
    assert all_prefixes("a b") == ["a", "a ", "a b"]

def test_string_with_numbers():
    assert all_prefixes("123") == ["1", "12", "123"]

def test_string_with_special_characters():
    assert all_prefixes("!@#") == ["!", "!@", "!@#"]

def test_string_with_repeated_characters():
    assert all_prefixes("aaa") == ["a", "aa", "aaa"]

def test_string_with_mixed_content():
    assert all_prefixes("a1!") == ["a", "a1", "a1!"]

@pytest.mark.parametrize("input_str,expected", [
    ("x", ["x"]),
    ("xy", ["x", "xy"]),
    ("abc", ["a", "ab", "abc"]),
    ("test", ["t", "te", "tes", "test"]),
    ("12345", ["1", "12", "123", "1234", "12345"])
])
def test_parametrized_cases(input_str, expected):
    assert all_prefixes(input_str) == expected

def test_unicode_string():
    assert all_prefixes("αβγ") == ["α", "αβ", "αβγ"]

def test_string_with_newlines():
    assert all_prefixes("a\nb") == ["a", "a\n", "a\nb"]

def test_string_with_tabs():
    assert all_prefixes("a\tb") == ["a", "a\t", "a\tb"]

def test_long_string():
    input_str = "abcdefghijklmnopqrstuvwxyz"
    expected = [input_str[:i+1] for i in range(len(input_str))]
    assert all_prefixes(input_str) == expected
