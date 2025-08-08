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

def test_empty_string():
    assert correct_bracketing("") == True

def test_single_opening_bracket():
    assert correct_bracketing("(") == False

def test_single_closing_bracket():
    assert correct_bracketing(")") == False

def test_simple_pair():
    assert correct_bracketing("()") == True

def test_nested_pairs():
    assert correct_bracketing("(())") == True

def test_multiple_pairs():
    assert correct_bracketing("()()") == True

def test_complex_nested():
    assert correct_bracketing("((()()))") == True

def test_unmatched_opening():
    assert correct_bracketing("((()") == False

def test_unmatched_closing():
    assert correct_bracketing("())") == False

def test_wrong_order():
    assert correct_bracketing(")(") == False

@pytest.mark.parametrize("brackets,expected", [
    ("", True),
    ("()", True),
    ("((()))", True),
    ("(()())", True),
    ("(", False),
    (")", False),
    (")(", False),
    ("(()", False),
    ("())", False),
    ("((())", False),
    ("(()))", False),
    ("(()()", False),
    ("())(", False)
])
def test_brackets_parametrized(brackets, expected):
    assert correct_bracketing(brackets) == expected

def test_long_sequence():
    assert correct_bracketing("(" * 1000 + ")" * 1000) == True

def test_alternating_sequence():
    assert correct_bracketing("()" * 1000) == True

def test_long_unbalanced():
    assert correct_bracketing("(" * 1000 + ")" * 999) == False
