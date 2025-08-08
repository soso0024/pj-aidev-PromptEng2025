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

def test_separate_paren_groups_valid_inputs(input_str, expected):
    assert separate_paren_groups(input_str) == expected

def separate_paren_groups(paren_string: str) -> List[str]:
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

@pytest.mark.parametrize("input_str,expected", [
    ("(()()) (()) ()", ["(()())", "(())", "()"]),
    ("", []),
    ("()", ["()"]),
    ("((()))", ["((()))"]),
    ("(()) ()", ["(())", "()"]),
    ("((())) ((()))", ["((()))", "((()))"]),
    ("(((()))) (()) () ((())())", ["(((())))", "(())", "()", "((())())"]),
])
def test_separate_paren_groups_valid_inputs(input_str, expected):
    assert separate_paren_groups(input_str) == expected

@pytest.mark.parametrize("input_str", [
    "(()",
    "())",
    "((())",
    ")()",
    "a()",
    "(a)",
    None,
])
def test_separate_paren_groups_invalid_inputs(input_str):
    if input_str is None:
        with pytest.raises(TypeError):
            separate_paren_groups(input_str)
    elif any(c not in '() ' for c in input_str):
        with pytest.raises(ValueError):
            separate_paren_groups(input_str)
    else:
        result = separate_paren_groups(input_str)
        for group in result:
            count = 0
            for c in group:
                if c == '(':
                    count += 1
                else:
                    count -= 1
                if count < 0:
                    pytest.fail("Invalid parentheses grouping")
            if count != 0:
                pytest.fail("Unbalanced parentheses")

def test_separate_paren_groups_deep_nesting():
    input_str = "(" * 100 + ")" * 100
    expected = ["(" * 100 + ")" * 100]
    assert separate_paren_groups(input_str) == expected

def test_separate_paren_groups_multiple_groups():
    input_str = "(())(())(())"
    expected = ["(())", "(())", "()"]
    result = separate_paren_groups(input_str)
    assert len(result) == len(expected)
    for group in result:
        assert group.count('(') == group.count(')')

def test_separate_paren_groups_whitespace():
    input_str = "  (())  (())  "
    expected = ["(())", "(())"]
    result = separate_paren_groups(input_str)
    assert len(result) == len(expected)
    for group in result:
        assert group.count('(') == group.count(')')

def test_separate_paren_groups_empty_groups():
    input_str = "()()()"
    expected = ["()", "()", "()"]
    assert separate_paren_groups(input_str) == expected