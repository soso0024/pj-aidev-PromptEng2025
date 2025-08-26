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
from typing import List, Optional

def test_longest_empty_list():
    assert longest([]) is None

def test_longest_single_string():
    assert longest(['hello']) == 'hello'

@pytest.mark.parametrize("strings,expected", [
    (['apple', 'banana', 'cherry'], 'cherry'),
    (['cat', 'dog', 'elephant'], 'elephant'),
    (['short', 'longer', 'longest'], 'longest')
])
def test_longest_multiple_strings(strings, expected):
    assert longest(strings) == expected

def test_longest_all_equal_length():
    assert longest(['abc', 'def', 'ghi']) in ['abc', 'def', 'ghi']

def test_longest_with_whitespace():
    assert longest(['  hello  ', 'world', '  python  ']) == '  hello  '

def test_longest_with_empty_strings():
    assert longest(['', 'non-empty', '']) == 'non-empty'