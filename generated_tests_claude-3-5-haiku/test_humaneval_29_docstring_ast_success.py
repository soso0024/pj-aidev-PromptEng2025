# Test cases for HumanEval/29
# Generated using Claude API

from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.
    >>> filter_by_prefix([], 'a')
    []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    """

    return [x for x in strings if x.startswith(prefix)]


# Generated test cases:
import pytest
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]

def test_empty_list():
    assert filter_by_prefix([], 'a') == []

def test_no_matches():
    assert filter_by_prefix(['bcd', 'cde'], 'a') == []

def test_some_matches():
    assert filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a') == ['abc', 'array']

def test_case_sensitive():
    assert filter_by_prefix(['Abc', 'abc'], 'a') == ['abc']
    assert filter_by_prefix(['Abc', 'abc'], 'A') == ['Abc']

def test_empty_prefix():
    assert filter_by_prefix(['abc', 'def', 'ghi'], '') == ['abc', 'def', 'ghi']

@pytest.mark.parametrize("strings,prefix,expected", [
    ([], 'test', []),
    (['hello', 'world'], 'h', ['hello']),
    (['python', 'pytest', 'programming'], 'p', ['python', 'pytest', 'programming']),
    (['UPPER', 'lower', 'MiXeD'], 'l', ['lower']),
    (['a', 'ab', 'abc'], 'ab', ['ab', 'abc'])
])
def test_parametrized_cases(strings, prefix, expected):
    assert filter_by_prefix(strings, prefix) == expected
