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
    assert all_prefixes('') == []

@pytest.mark.parametrize("input_string,expected", [
    ('abc', ['a', 'ab', 'abc']),
    ('hello', ['h', 'he', 'hel', 'hell', 'hello']),
    ('python', ['p', 'py', 'pyt', 'pyth', 'pytho', 'python']),
    ('x', ['x'])
])
def test_all_prefixes_normal_cases(input_string, expected):
    assert all_prefixes(input_string) == expected

def test_all_prefixes_single_character():
    assert all_prefixes('a') == ['a']

def test_all_prefixes_whitespace_string():
    assert all_prefixes('   ') == [' ', '  ', '   ']

def test_all_prefixes_non_string_input():
    with pytest.raises(TypeError):
        all_prefixes(123)
