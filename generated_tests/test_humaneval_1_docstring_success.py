# Test cases for HumanEval/1
# Generated using Claude API

from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    result = []
    current_string = []
    current_depth = 0

    for c in paren_string:
        if c == '(':
            current_depth += 1
            current_string.append(c)
        elif c == ')':
            current_depth -= 1
            current_string.append(c)

            if current_depth == 0:
                result.append(''.join(current_string))
                current_string.clear()

    return result


# Generated test cases:
import pytest
from typing import List


@pytest.mark.parametrize("input_str,expected", [
    ("()", ["()"]),
    ("(())", ["(())"]),
    ("()()", ["()", "()"]),
    ("((()))", ["((()))"]),
    ("(( )( ))", ["(()())"]),
    ("( ) (( )) (( )( ))", ["()", "(())", "(()())"]),
    ("", []),
    ("     ", []),
    ("(     )", ["()"]),
    ("(() ()) ()", ["(()())", "()"]),
    ("(())(())", ["(())", "(())"]),
])
def test_separate_paren_groups_valid_inputs(input_str: str, expected: List[str]):
    assert separate_paren_groups(input_str) == expected


@pytest.mark.parametrize("input_str", [
    "(", 
    ")", 
    "(()", 
    "())", 
    "((())",
    "()))",
    ")(",
    ")()",
])
def test_separate_paren_groups_unbalanced(input_str: str):
    result = separate_paren_groups(input_str)
    # Unbalanced parentheses should result in either empty list or partial groups
    assert all(result.count('(') == result.count(')') for result in result)


@pytest.mark.parametrize("input_str", [
    "abc",
    "a(b)c",
    "123",
    "@#$",
    "",
])
def test_separate_paren_groups_non_paren_chars(input_str: str):
    result = separate_paren_groups(input_str)
    assert isinstance(result, list)
    # Should handle non-parentheses characters gracefully
    assert all('(' in group and ')' in group for group in result)


def test_separate_paren_groups_nested_complex():
    input_str = "((())) (()) () ((()()))"
    expected = ["((()))", "(())", "()", "((()()))"]
    assert separate_paren_groups(input_str) == expected


def test_separate_paren_groups_with_spaces():
    input_str = "(   )  ((  ))  ((  )(  ))"
    expected = ["()", "(())", "(()())"]
    assert separate_paren_groups(input_str) == expected


def test_separate_paren_groups_empty_input():
    assert separate_paren_groups("") == []
    assert separate_paren_groups(" " * 10) == []
