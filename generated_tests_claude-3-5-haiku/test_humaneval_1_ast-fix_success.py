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
from typing import List
import pytest

def separate_paren_groups(paren_string: str) -> List[str]:
    result = []
    current_string = []
    current_depth = 0

    for c in paren_string:
        if c == ' ':
            continue
        if c == '(':
            current_depth += 1
            current_string.append(c)
        elif c == ')':
            current_depth -= 1
            current_string.append(c)

            if current_depth < 0:
                raise ValueError("Unbalanced parentheses")

            if current_depth == 0:
                result.append(''.join(current_string))
                current_string.clear()

    if current_depth > 0:
        raise ValueError("Unbalanced parentheses")

    return result

def test_separate_paren_groups_basic():
    assert separate_paren_groups('(())') == ['(())']

def test_separate_paren_groups_multiple():
    assert separate_paren_groups('(())(())') == ['(())', '(())']

def test_separate_paren_groups_nested():
    assert separate_paren_groups('((()))') == ['((()))']

def test_separate_paren_groups_complex():
    assert separate_paren_groups('(()())(())') == ['(()())', '(())']

def test_separate_paren_groups_empty():
    assert separate_paren_groups('') == []

def test_separate_paren_groups_single_group():
    assert separate_paren_groups('()') == ['()']

@pytest.mark.parametrize("input_str,expected", [
    ('(())', ['(())']),
    ('(())(())', ['(())', '(())']),
    ('((()))', ['((()))']),
    ('(()())(())', ['(()())', '(())']),
    ('', []),
    ('()', ['()'])
])
def test_separate_paren_groups_parametrized(input_str, expected):
    assert separate_paren_groups(input_str) == expected

def test_separate_paren_groups_unbalanced():
    with pytest.raises(ValueError):
        separate_paren_groups('((')
    with pytest.raises(ValueError):
        separate_paren_groups('))')