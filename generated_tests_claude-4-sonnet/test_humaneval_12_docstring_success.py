# Test cases for HumanEval/12
# Generated using Claude API

from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    >>> longest([])

    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    """

    if not strings:
        return None

    maxlen = max(len(x) for x in strings)
    for s in strings:
        if len(s) == maxlen:
            return s


# Generated test cases:
import pytest
from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None

    maxlen = max(len(x) for x in strings)
    for s in strings:
        if len(s) == maxlen:
            return s


def test_empty_list():
    assert longest([]) is None


def test_single_string():
    assert longest(['hello']) == 'hello'


def test_single_empty_string():
    assert longest(['']) == ''


def test_multiple_strings_different_lengths():
    assert longest(['a', 'bb', 'ccc']) == 'ccc'


def test_multiple_strings_same_length_returns_first():
    assert longest(['abc', 'def', 'ghi']) == 'abc'


def test_mixed_lengths_with_duplicates():
    assert longest(['a', 'bb', 'cc', 'ddd']) == 'ddd'


def test_longest_at_beginning():
    assert longest(['longest', 'a', 'bb']) == 'longest'


def test_longest_at_end():
    assert longest(['a', 'bb', 'longest']) == 'longest'


def test_longest_in_middle():
    assert longest(['a', 'longest', 'bb']) == 'longest'


def test_multiple_longest_same_length():
    assert longest(['abc', 'def', 'xyz']) == 'abc'


def test_empty_strings_mixed():
    assert longest(['', 'a', '']) == 'a'


def test_all_empty_strings():
    assert longest(['', '', '']) == ''


@pytest.mark.parametrize("input_list,expected", [
    (['a'], 'a'),
    (['hello', 'world'], 'hello'),
    (['short', 'medium', 'very_long_string'], 'very_long_string'),
    (['same', 'size'], 'same'),
    (['', 'x'], 'x'),
    (['x', ''], 'x')
])
def test_parametrized_cases(input_list, expected):
    assert longest(input_list) == expected


def test_special_characters():
    assert longest(['!@#', '$$$$', '%']) == '$$$$'


def test_unicode_strings():
    assert longest(['café', 'naïve', 'résumé']) == 'résumé'


def test_whitespace_strings():
    assert longest([' ', '  ', '   ']) == '   '


def test_mixed_whitespace_and_text():
    assert longest(['a', ' b ', '  c  ']) == '  c  '