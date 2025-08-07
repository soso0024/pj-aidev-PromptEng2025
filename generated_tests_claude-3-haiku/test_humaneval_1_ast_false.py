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
    assert separate_paren_groups("") == []

def test_separate_paren_groups_single_pair():
    assert separate_paren_groups("(test)") == ["(test)"]

def test_separate_paren_groups_multiple_pairs():
    assert separate_paren_groups("(test)(another)") == ["(test)", "(another)"]

def test_separate_paren_groups_nested_pairs():
    assert separate_paren_groups("(test(nested))") == ["(test(nested))"]

def test_separate_paren_groups_mixed_pairs():
    assert separate_paren_groups("(test)(another(nested))") == ["(test)", "(another(nested))"]

def test_separate_paren_groups_unbalanced_open():
    with pytest.raises(ValueError):
        separate_paren_groups("(test(unbalanced")

def test_separate_paren_groups_unbalanced_close():
    with pytest.raises(ValueError):
        separate_paren_groups("test)unbalanced)")