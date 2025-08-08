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
from parse_nested_parens import parse_nested_parens


def validate_parens(s: str) -> bool:
    count = 0
    for c in s:
        if c == '(':
            count += 1
        elif c == ')':
            count -= 1
        elif c not in ' ':
            return False
        if count < 0:
            return False
    return count == 0


@pytest.mark.parametrize("input_str,expected", [
    ("(()()) ((())) () ((())()())", [2, 3, 1, 3]),
    ("()", [1]),
    ("((()))", [3]),
    ("(()) (()) (())", [2, 2, 2]),
    ("", []),
    ("   ", []),
    ("(((())))", [4]),
    ("() () () ()", [1, 1, 1, 1]),
    ("(()()) (()())", [2, 2]),
    ("((())(()))", [3]),
])
def test_parse_nested_parens_valid_inputs(input_str, expected):
    assert parse_nested_parens(input_str) == expected


@pytest.mark.parametrize("invalid_input", [
    "((",
    "))",
    "(()",
    "())",
    "(() )",
    "( ())",
    "(())) (()",
])
def test_parse_nested_parens_invalid_inputs(invalid_input):
    if not validate_parens(invalid_input):
        result = parse_nested_parens(invalid_input)
        assert False, f"Expected ValueError but got result: {result}"


def test_parse_nested_parens_empty_groups():
    assert parse_nested_parens("() () () ") == [1, 1, 1]


def test_parse_nested_parens_single_space():
    assert parse_nested_parens(" ") == []


def test_parse_nested_parens_multiple_spaces():
    assert parse_nested_parens("   ") == []


def test_parse_nested_parens_complex_nesting():
    assert parse_nested_parens("(((()))) ((())()) (())") == [4, 3, 2]


def test_parse_nested_parens_single_char():
    result = parse_nested_parens("(")
    assert False, f"Expected ValueError but got result: {result}"


def test_parse_nested_parens_non_paren_chars():
    result = parse_nested_parens("(a)")
    assert False, f"Expected ValueError but got result: {result}"


def test_parse_nested_parens_mixed_spaces():
    assert parse_nested_parens("()  ()   ()    ()") == [1, 1, 1, 1]