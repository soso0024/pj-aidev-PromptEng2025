# Test cases for HumanEval/61
# Generated using Claude API



def correct_bracketing(brackets: str):
    """ brackets is a string of "(" and ")".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing("(")
    False
    >>> correct_bracketing("()")
    True
    >>> correct_bracketing("(()())")
    True
    >>> correct_bracketing(")(()")
    False
    """

    depth = 0
    for b in brackets:
        if b == "(":
            depth += 1
        else:
            depth -= 1
        if depth < 0:
            return False
    return depth == 0


# Generated test cases:
from your_module import correct_bracketing
import pytest

@pytest.mark.parametrize("brackets, expected", [
    ("()", True),
    ("(()())", True),
    ("(", False),
    (")", False),
    ("(())", True),
    (")(()", False),
    ("((()))", True),
    ("(())()", True),
    ("", True),
    ("(())(", False),
    (")())", False),
    ("((())", False),
    ("()())", False),
])
def test_correct_bracketing(brackets, expected):
    assert correct_bracketing(brackets) == expected

def test_correct_bracketing_raises_error_on_non_string():
    with pytest.raises(TypeError):
        correct_bracketing(123)