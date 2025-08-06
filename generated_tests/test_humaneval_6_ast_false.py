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

@pytest.mark.parametrize("input_str,expected", [
    ("()", [1]),
    ("(())", [2]),
    ("(()) ()", [2, 1]),
    ("((()))", [3]),
    ("(() ())", [2]),
    ("(()(()))", [3]),
    ("(()) () ((()))", [2, 1, 3]),
    ("", []),
    ("   ", []),
    ("((())) () (()) ((())())", [3, 1, 2, 3]),
])
def test_parse_nested_parens_valid(input_str: str, expected: List[int]):
    assert parse_nested_parens(input_str) == expected

@pytest.mark.parametrize("input_str", [
    "(", 
    ")", 
    "(()", 
    "())", 
    "(() ()) )",
    "((()) () (",
])
def test_parse_nested_parens_unbalanced(input_str: str):
    result = parse_nested_parens(input_str)
    for depth in result:
        assert depth >= 0

@pytest.mark.parametrize("input_str,expected", [
    ("(a)", [1]),
    ("((b))", [2]),
    ("123", [0]),
    ("(1) (2) (3)", [1, 1, 1]),
])
def test_parse_nested_parens_with_content(input_str: str, expected: List[int]):
    assert parse_nested_parens(input_str) == expected

@pytest.mark.parametrize("input_str,expected", [
    ("()()()", [1]),
    ("((())", [2]),
    ("((()))", [3]),
])
def test_parse_nested_parens_malformed(input_str: str, expected: List[int]):
    assert parse_nested_parens(input_str) == expected

def test_parse_nested_parens_special_chars():
    input_str = "(() ()) (\t) (!@#$)"
    expected = [2, 1, 1]
    assert parse_nested_parens(input_str) == expected

def test_parse_nested_parens_multiple_spaces():
    input_str = "(())    ()      ((()))"
    expected = [2, 1, 3]
    assert parse_nested_parens(input_str) == expected