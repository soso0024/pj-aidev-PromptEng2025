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
import pytest

def correct_bracketing(brackets: str):
    depth = 0
    for b in brackets:
        if b == "(":
            depth += 1
        else:
            depth -= 1
        if depth < 0:
            return False
    return depth == 0

@pytest.mark.parametrize("brackets,expected", [
    ("", True),
    ("()", True),
    ("(())", True),
    ("()()", True),
    ("((()))", True),
    ("(()())", True),
    ("(()(()))", True),
    ("(", False),
    (")", False),
    ("((", False),
    ("))", False),
    ("())", False),
    ("(()", False),
    (")(", False),
    (")())", False),
    ("((())", False),
    ("()())", False),
    ("(())()", True),
    ("((())())", True),
    ("((((()))))", True),
    ("((((()))", False),
    ("()))))", False),
    ("((((((", False),
    ("))))))", False),
    ("()" * 1000, True),
])
def test_correct_bracketing(brackets, expected):
    assert correct_bracketing(brackets) == expected