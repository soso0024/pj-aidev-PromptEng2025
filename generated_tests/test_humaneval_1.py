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

def separate_paren_groups(s: str) -> List[str]:
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    
    if not s:
        return []

    result = []
    current = []
    count = 0
    
    for char in s:
        if char == '(':
            count += 1
            current.append(char)
        elif char == ')':
            count -= 1
            current.append(char)
        elif char == ' ' and count == 0 and current:
            result.append(''.join(current))
            current = []
        elif char != ' ':
            raise ValueError("Invalid character in input")
            
        if count < 0:
            raise ValueError("Invalid parentheses sequence")
            
    if current:
        if count != 0:
            raise ValueError("Unmatched parentheses")
        result.append(''.join(current))
        
    return result

@pytest.mark.parametrize("input_str,expected", [
    ("(()()) (()) ()", ["(()())", "(())", "()"]),
    ("", []),
    ("()", ["()"]),
    ("((()))", ["((()))"]),
    ("(()) ()", ["(())", "()"]),
    ("((())) (()) ()", ["((()))", "(())", "()"]),
    ("(((()))) (()) () ((())())", ["(((())))", "(())", "()", "((())())"]),
])
def test_separate_paren_groups_valid_inputs(input_str: str, expected: List[str]):
    assert separate_paren_groups(input_str) == expected

@pytest.mark.parametrize("input_str", [
    "((",
    ")",
    "())",
    "(()",
    ")(",
    "hello",
    "( )",
    "(a)",
    None
])
def test_separate_paren_groups_invalid_inputs(input_str):
    with pytest.raises((ValueError, TypeError)):
        separate_paren_groups(input_str)

def test_separate_paren_groups_nested():
    input_str = "((()())()) ((())) ((())())"
    expected = ["((()())())", "((()))", "((())())"]
    assert separate_paren_groups(input_str) == expected

def test_separate_paren_groups_single_char():
    with pytest.raises(ValueError):
        separate_paren_groups("(")
    with pytest.raises(ValueError):
        separate_paren_groups(")")

def test_separate_paren_groups_empty():
    assert separate_paren_groups("") == []

def test_separate_paren_groups_multiple_empty_spaces():
    input_str = "(())    ()      (())"
    expected = ["(())", "()", "(())"]
    assert separate_paren_groups(input_str) == expected

def test_separate_paren_groups_long_sequence():
    input_str = "(" * 100 + ")" * 100
    expected = ["(" * 100 + ")" * 100]
    assert separate_paren_groups(input_str) == expected