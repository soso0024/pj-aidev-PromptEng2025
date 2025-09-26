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

def test_empty_string():
    assert separate_paren_groups("") == []

def test_single_empty_group():
    assert separate_paren_groups("()") == ["()"]

def test_single_empty_group_with_spaces():
    assert separate_paren_groups("( )") == ["()"]

def test_multiple_empty_groups():
    assert separate_paren_groups("()()") == ["()", "()"]

def test_multiple_empty_groups_with_spaces():
    assert separate_paren_groups("( ) ( )") == ["()", "()"]

def test_nested_groups():
    assert separate_paren_groups("(())") == ["(())"]

def test_nested_groups_with_spaces():
    assert separate_paren_groups("(( ))") == ["(())"]

def test_complex_nested_groups():
    assert separate_paren_groups("((()))") == ["((()))"]

def test_multiple_nested_groups():
    assert separate_paren_groups("(())(())") == ["(())", "(())"]

def test_mixed_groups():
    assert separate_paren_groups("()(())") == ["()", "(())"]

def test_example_from_docstring():
    assert separate_paren_groups("( ) (( )) (( )( ))") == ["()", "(())", "(()())"]

def test_complex_nested_structure():
    assert separate_paren_groups("((()())())") == ["((()())())"]

def test_multiple_complex_groups():
    assert separate_paren_groups("((()))(()())") == ["((()))", "(()())"]

def test_many_spaces():
    assert separate_paren_groups("  (   )   (  (  )  )  ") == ["()", "(())"]

def test_deeply_nested():
    assert separate_paren_groups("(((())))") == ["(((())))"]

def test_multiple_deeply_nested():
    assert separate_paren_groups("(((())))(((())))")== ["(((())))", "(((())))"]

@pytest.mark.parametrize("input_str,expected", [
    ("()", ["()"]),
    ("(())", ["(())"]),
    ("()()", ["()", "()"]),
    ("( ) ( )", ["()", "()"]),
    ("(( ))", ["(())"]),
    ("((()))", ["((()))"]),
    ("(()())", ["(()())"]),
    ("()(())", ["()", "(())"]),
    ("(()(()))", ["(()(()))"]),
])
def test_parametrized_cases(input_str, expected):
    assert separate_paren_groups(input_str) == expected

def test_only_spaces():
    assert separate_paren_groups("   ") == []

def test_single_group_many_levels():
    assert separate_paren_groups("(((((())))))") == ["(((((())))))"]

def test_alternating_simple_and_complex():
    assert separate_paren_groups("()(())()(())") == ["()", "(())", "()", "(())"]
