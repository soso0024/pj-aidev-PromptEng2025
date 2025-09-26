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
    ("((()))", [3]),
    ("() (())", [1, 2]),
    ("(()(()))", [3]),
    ("(()()) (())", [2, 2]),
    ("((())()) ((())())", [3, 3]),
    ("()()()", [1]),
    ("(((()))))", [4]),
    ("() () ()", [1, 1, 1]),
    ("(()(()()))", [3]),
])
def test_parse_nested_parens_normal_cases(input_str, expected):
    assert parse_nested_parens(input_str) == expected

def test_empty_string():
    assert parse_nested_parens("") == []

def test_only_spaces():
    assert parse_nested_parens("   ") == []

def test_single_open_paren():
    assert parse_nested_parens("(") == [1]

def test_single_close_paren():
    assert parse_nested_parens(")") == [0]

def test_multiple_spaces_between_groups():
    assert parse_nested_parens("()    (())") == [1, 2]

def test_leading_and_trailing_spaces():
    assert parse_nested_parens("  ()  ") == [1]

def test_unbalanced_parens():
    assert parse_nested_parens("(()") == [2]
    assert parse_nested_parens("())") == [1]

def test_complex_nested_structure():
    assert parse_nested_parens("((((())))) (()) ()") == [5, 2, 1]

def test_mixed_balanced_unbalanced():
    assert parse_nested_parens("(() )()") == [2, 0]

def test_deeply_nested():
    deep_parens = "(" * 10 + ")" * 10
    assert parse_nested_parens(deep_parens) == [10]

def test_multiple_groups_with_varying_depths():
    assert parse_nested_parens("() (()) ((()))") == [1, 2, 3]