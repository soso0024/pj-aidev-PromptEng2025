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

def test_separate_paren_groups_empty_string():
    assert separate_paren_groups('') == []

def test_separate_paren_groups_no_parens():
    assert separate_paren_groups('hello world') == []

def test_separate_paren_groups_single_group():
    assert separate_paren_groups('(hello)') == ['(hello)']

def test_separate_paren_groups_multiple_groups():
    assert separate_paren_groups('(hello)(world)(foo)') == ['(hello)', '(world)', '(foo)']

def test_separate_paren_groups_nested_groups():
    assert separate_paren_groups('((a)(b))(c)') == ['((a)(b))', '(c)']

def test_separate_paren_groups_unbalanced_parens():
    with pytest.raises(ValueError):
        separate_paren_groups('(hello')

def test_separate_paren_groups_leading_closing_paren():
    with pytest.raises(ValueError):
        separate_paren_groups(')hello(')

@pytest.mark.parametrize("input,expected", [
    ('(a(b)c)(d(e)f)', ['(a(b)c)', '(d(e)f)']),
    ('(ab)(cd(ef))', ['(ab)', '(cd(ef))']),
    ('(a)b(c)d(e)', ['(a)', '(c)', '(e)'])
])
def test_separate_paren_groups_parameterized(input, expected):
    assert separate_paren_groups(input) == expected

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

    if current_depth != 0:
        raise ValueError("Unbalanced parentheses")

    return result