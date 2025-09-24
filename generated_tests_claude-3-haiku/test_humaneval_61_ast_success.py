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

def test_correct_bracketing_empty_string():
    assert correct_bracketing("") == True

def test_correct_bracketing_single_open_bracket():
    assert correct_bracketing("(") == False

def test_correct_bracketing_single_close_bracket():
    assert correct_bracketing(")") == False

def test_correct_bracketing_balanced_brackets():
    assert correct_bracketing("()") == True
    assert correct_bracketing("(())") == True
    assert correct_bracketing("((()))") == True

def test_correct_bracketing_unbalanced_brackets():
    assert correct_bracketing("(()") == False
    assert correct_bracketing(")()") == False
    assert correct_bracketing("(())()") == True
    assert correct_bracketing("((())())") == True
    assert correct_bracketing("(()())()") == True

@pytest.mark.parametrize("input,expected", [
    ("", True),
    ("(", False),
    (")", False),
    ("()", True),
    ("(())", True),
    ("((()))", True),
    ("(()", False),
    (")()", False),
    ("(())()", True),
    ("((())())", True),
    ("(()())()", True)
])
def test_correct_bracketing_parametrized(input, expected):
    assert correct_bracketing(input) == expected

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
