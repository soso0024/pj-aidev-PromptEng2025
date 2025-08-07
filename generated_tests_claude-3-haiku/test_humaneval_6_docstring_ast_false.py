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
from typing import List
import pytest

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

def test_parse_nested_parens():
    assert parse_nested_parens('(()()) ((())) () ((())()())') == [2, 3, 1, 3]
    assert parse_nested_parens('()') == [1]
    assert parse_nested_parens('(())') == [2]
    assert parse_nested_parens('()(())') == [1, 2]
    assert parse_nested_parens('') == []
    assert parse_nested_parens('  ') == []
    assert parse_nested_parens('(') == [1]
    assert parse_nested_parens(')') == [0]
    assert parse_nested_parens('()()') == [1, 1]
    assert parse_nested_parens('(())(())') == [2, 2]
    assert parse_nested_parens('((())))') == [3, 0]
    assert parse_nested_parens('((())') == [3]

@pytest.mark.parametrize("input,expected", [
    ('(()()) ((())) () ((())()())', [2, 3, 1, 3]),
    ('()', [1]),
    ('(())', [2]),
    ('()(())', [1, 2]),
    ('', []),
    ('  ', []),
    ('(', [1]),
    (')', [0]),
    ('()()', [1, 1]),
    ('(())(())', [2, 2]),
    ('((()))))', [3, 0]),
    ('((())', [3])
])
def test_parse_nested_parens_parametrized(input, expected):
    assert parse_nested_parens(input) == expected

def test_parse_nested_parens_edge_cases():
    with pytest.raises(TypeError):
        parse_nested_parens(123)
    with pytest.raises(TypeError):
        parse_nested_parens([])
    with pytest.raises(TypeError):
        parse_nested_parens(None)