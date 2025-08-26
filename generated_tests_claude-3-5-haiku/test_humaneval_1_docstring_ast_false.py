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

            if current_depth == 0:
                result.append(''.join(current_string))
                current_string.clear()

    return result

def test_separate_paren_groups_basic():
    assert separate_paren_groups('( ) (( )) (( )( ))') == ['()', '(())', '(()())']

def test_separate_paren_groups_empty_string():
    assert separate_paren_groups('') == []

def test_separate_paren_groups_single_group():
    assert separate_paren_groups('(hello)') == ['(hello)']

def test_separate_paren_groups_multiple_groups():
    assert separate_paren_groups('() (()) ((()))') == ['()', '(())', '((()))']

def test_separate_paren_groups_with_spaces():
    assert separate_paren_groups(' ( )  (( ))  (( )( )) ') == ['()', '(())', '(()())']

def test_separate_paren_groups_nested():
    assert separate_paren_groups('((()()))') == ['((()()))']

import pytest

@pytest.mark.parametrize("input_str,expected", [
    ('( ) (( )) (( )( ))', ['()', '(())', '(()())']),
    ('', []),
    ('(hello)', ['(hello)']),
    ('() (()) ((()))', ['()', '(())', '((()))']),
    (' ( )  (( ))  (( )( )) ', ['()', '(())', '(()())']),
    ('((()()))', ['((()()))'])
])
def test_separate_paren_groups_parametrized(input_str, expected):
    assert separate_paren_groups(input_str) == expected