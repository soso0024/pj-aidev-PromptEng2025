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

def test_all_prefixes_normal_cases():
    assert all_prefixes("hello") == ["h", "he", "hel", "hell", "hello"]
    assert all_prefixes("abc") == ["a", "ab", "abc"]

def test_all_prefixes_empty_string():
    assert all_prefixes("") == []

def test_all_prefixes_single_character():
    assert all_prefixes("x") == ["x"]

@pytest.mark.parametrize("input_string,expected", [
    ("python", ["p", "py", "pyt", "pyth", "pytho", "python"]),
    ("", []),
    ("a", ["a"]),
    ("programming", ["p", "pr", "pro", "prog", "progr", "progra", "program", "programm", "programmi", "programmin", "programming"])
])
def test_all_prefixes_parametrized(input_string, expected):
    assert all_prefixes(input_string) == expected

def test_all_prefixes_with_spaces():
    assert all_prefixes("hello world") == ["h", "he", "hel", "hell", "hello", "hello ", "hello w", "hello wo", "hello wor", "hello worl", "hello world"]

def test_all_prefixes_with_special_characters():
    assert all_prefixes("a!b@c#") == ["a", "a!", "a!b", "a!b@", "a!b@c", "a!b@c#"]
