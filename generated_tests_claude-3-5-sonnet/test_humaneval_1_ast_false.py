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

def test_separate_paren_groups_valid(input_str: str, expected: List[str]):
    assert separate_paren_groups(input_str) == expected

test_separate_paren_groups_valid.parametrize = pytest.mark.parametrize("input_str,expected", [
    ("(())", ["(())"]),
    ("()()", ["()", "()"]),
    ("((()))", ["((()))"]),
    ("((())())", ["((())())"]),
    ("((()))(())", ["((()))", "(())"]),
    ("(((()))((())))", ["((()))", "((()))"]),
    ("()", ["()"]),
    ("((()())(())())", ["((()())(())())"]),
    ("(()(()))", ["(()(()))"]),
    ("(()())(())", ["(()())", "(())"]),
    ("", []),
    ("((())())((())())", ["((())())", "((())())"]),
])

def test_separate_paren_groups_invalid(invalid_input):
    with pytest.raises((ValueError, TypeError)):
        separate_paren_groups(invalid_input)

test_separate_paren_groups_invalid.parametrize = pytest.mark.parametrize("invalid_input", [
    "(",
    ")",
    "())",
    "(()",
    ")(",
    "a()",
    "(a)",
    "((a))",
    None,
])

def test_separate_paren_groups_empty():
    assert separate_paren_groups("") == []

def test_separate_paren_groups_nested():
    input_str = "((())(()))(((())))"
    expected = ["((())(()))", "((()))"]
    assert separate_paren_groups(input_str) == expected

def test_separate_paren_groups_multiple():
    input_str = "()(())(((())))"
    expected = ["()", "(())", "((()))"]
    assert separate_paren_groups(input_str) == expected

def test_separate_paren_groups_complex():
    input_str = "(()(()()))(())(((())))"
    expected = ["(()(()()))", "(())", "((()))"]
    assert separate_paren_groups(input_str) == expected

def separate_paren_groups(paren_string: str) -> List[str]:
    result = []
    current_string = []
    current_depth = 0

    if not isinstance(paren_string, str):
        raise TypeError("Input must be a string")

    for c in paren_string:
        if c not in '()':
            raise ValueError("Invalid character in input")
        if c == '(':
            current_depth += 1
            current_string.append(c)
        elif c == ')':
            current_depth -= 1
            if current_depth < 0:
                raise ValueError("Unmatched closing parenthesis")
            current_string.append(c)

            if current_depth == 0:
                result.append(''.join(current_string))
                current_string.clear()

    if current_depth != 0:
        raise ValueError("Unmatched opening parenthesis")

    return result