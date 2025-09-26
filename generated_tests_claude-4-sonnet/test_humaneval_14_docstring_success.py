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

def all_prefixes(string: str) -> List[str]:
    result = []
    for i in range(len(string)):
        result.append(string[:i+1])
    return result

def test_all_prefixes_empty_string():
    assert all_prefixes("") == []

def test_all_prefixes_single_character():
    assert all_prefixes("a") == ["a"]

def test_all_prefixes_two_characters():
    assert all_prefixes("ab") == ["a", "ab"]

def test_all_prefixes_three_characters():
    assert all_prefixes("abc") == ["a", "ab", "abc"]

def test_all_prefixes_longer_string():
    assert all_prefixes("hello") == ["h", "he", "hel", "hell", "hello"]

def test_all_prefixes_with_spaces():
    assert all_prefixes("a b") == ["a", "a ", "a b"]

def test_all_prefixes_with_numbers():
    assert all_prefixes("123") == ["1", "12", "123"]

def test_all_prefixes_with_special_characters():
    assert all_prefixes("!@#") == ["!", "!@", "!@#"]

def test_all_prefixes_with_repeated_characters():
    assert all_prefixes("aaa") == ["a", "aa", "aaa"]

def test_all_prefixes_mixed_case():
    assert all_prefixes("AbC") == ["A", "Ab", "AbC"]

@pytest.mark.parametrize("input_str,expected", [
    ("x", ["x"]),
    ("xy", ["x", "xy"]),
    ("test", ["t", "te", "tes", "test"]),
    ("python", ["p", "py", "pyt", "pyth", "pytho", "python"])
])
def test_all_prefixes_parametrized(input_str, expected):
    assert all_prefixes(input_str) == expected

def test_all_prefixes_return_type():
    result = all_prefixes("test")
    assert isinstance(result, list)
    assert all(isinstance(prefix, str) for prefix in result)

def test_all_prefixes_unicode():
    assert all_prefixes("αβγ") == ["α", "αβ", "αβγ"]

def test_all_prefixes_newline():
    assert all_prefixes("a\nb") == ["a", "a\n", "a\nb"]
