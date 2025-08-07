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

@pytest.mark.parametrize("input_string,expected", [
    ("hello", ["h", "he", "hel", "hell", "hello"]),
    ("python", ["p", "py", "pyt", "pyth", "pytho", "python"]),
    ("a", ["a"]),
    ("ab", ["a", "ab"])
])
def test_all_prefixes_normal_cases(input_string, expected):
    assert all_prefixes(input_string) == expected

def test_all_prefixes_type_error():
    with pytest.raises(TypeError):
        all_prefixes(123)

def all_prefixes(string: str) -> list[str]:
    result = []

    for i in range(len(string)):
        result.append(string[:i+1])
    return result
