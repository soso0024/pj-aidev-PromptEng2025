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

def test_all_prefixes_normal_case():
    assert all_prefixes('abc') == ['a', 'ab', 'abc']

def test_all_prefixes_single_char():
    assert all_prefixes('x') == ['x']

def test_all_prefixes_empty_string():
    assert all_prefixes('') == []

@pytest.mark.parametrize("input_str,expected", [
    ('hello', ['h', 'he', 'hel', 'hell', 'hello']),
    ('python', ['p', 'py', 'pyt', 'pyth', 'pytho', 'python']),
    ('a', ['a']),
    ('', [])
])
def test_all_prefixes_parametrized(input_str, expected):
    assert all_prefixes(input_str) == expected

def test_all_prefixes_unicode():
    assert all_prefixes('café') == ['c', 'ca', 'caf', 'café']

def test_all_prefixes_whitespace():
    assert all_prefixes(' test ') == [' ', ' t', ' te', ' tes', ' test', ' test ']
