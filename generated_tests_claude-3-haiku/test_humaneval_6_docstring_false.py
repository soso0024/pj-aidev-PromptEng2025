# Test cases for HumanEval/6
# Generated using Claude API

from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    def parse_paren_group(s):
        depth = 0
        max_depth = 0
        for c in s:
            if c == '(':
                depth += 1
                max_depth = max(depth, max_depth)
            else:
                depth -= 1

        return max_depth

    return [parse_paren_group(x) for x in paren_string.split(' ') if x]


# Generated test cases:
import pytest
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    def parse_paren_group(s):
        depth = 0
        max_depth = 0
        for c in s:
            if c == '(':
                depth += 1
                max_depth = max(depth, max_depth)
            else:
                depth -= 1

        return max_depth

    return [parse_paren_group(x) for x in paren_string.split(' ') if x]

@pytest.mark.parametrize("paren_string,expected", [
    ('(()()) ((())) () ((())()())', [2, 3, 1, 3]),
    ('()', [1]),
    ('(())', [2]),
    ('(((())))', [4]),
    ('', []),
    ('(', [1]),
    (')', [0]),
    ('(())()', [2, 1]),
    ('(()()) ((())) ()', [2, 3, 1]),
    ('(()()) ((())) () ((())()()) ()', [2, 3, 1, 3, 1]),
])
def test_parse_nested_parens(paren_string, expected):
    assert parse_nested_parens(paren_string) == expected

def test_parse_nested_parens_empty_string():
    assert parse_nested_parens('') == []

def test_parse_nested_parens_single_paren():
    assert parse_nested_parens('(') == [1]
    assert parse_nested_parens(')') == [0]

def test_parse_nested_parens_single_group():
    assert parse_nested_parens('(()())') == [2]
    assert parse_nested_parens('((()))') == [3]