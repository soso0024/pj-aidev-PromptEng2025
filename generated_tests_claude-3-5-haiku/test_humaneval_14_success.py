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

def test_all_prefixes_normal_cases():
    assert all_prefixes("hello") == ["h", "he", "hel", "hell", "hello"]
    assert all_prefixes("a") == ["a"]
    assert all_prefixes("") == []

def test_all_prefixes_unicode():
    assert all_prefixes("café") == ["c", "ca", "caf", "café"]

@pytest.mark.parametrize("input_string,expected", [
    ("python", ["p", "py", "pyt", "pyth", "pytho", "python"]),
    ("", []),
    ("x", ["x"]),
    ("123", ["1", "12", "123"])
])
def test_all_prefixes_parametrized(input_string, expected):
    assert all_prefixes(input_string) == expected

def test_all_prefixes_type_error():
    with pytest.raises(TypeError):
        all_prefixes(123)
