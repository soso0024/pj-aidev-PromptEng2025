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

def test_correct_bracketing_empty_string():
    assert correct_bracketing("") == True

def test_correct_bracketing_single_opening():
    assert correct_bracketing("(") == False

def test_correct_bracketing_single_closing():
    assert correct_bracketing(")") == False

def test_correct_bracketing_simple_pair():
    assert correct_bracketing("()") == True

def test_correct_bracketing_nested():
    assert correct_bracketing("(())") == True

def test_correct_bracketing_multiple_pairs():
    assert correct_bracketing("()()") == True

def test_correct_bracketing_complex_nested():
    assert correct_bracketing("(()())") == True

def test_correct_bracketing_wrong_order():
    assert correct_bracketing(")(") == False

def test_correct_bracketing_starts_with_closing():
    assert correct_bracketing(")(()") == False

def test_correct_bracketing_ends_with_opening():
    assert correct_bracketing("(()((") == False

def test_correct_bracketing_unbalanced_more_opening():
    assert correct_bracketing("(((") == False

def test_correct_bracketing_unbalanced_more_closing():
    assert correct_bracketing(")))") == False

def test_correct_bracketing_mixed_unbalanced():
    assert correct_bracketing("((())") == False

def test_correct_bracketing_complex_wrong():
    assert correct_bracketing("(()(") == False

@pytest.mark.parametrize("brackets,expected", [
    ("", True),
    ("(", False),
    (")", False),
    ("()", True),
    ("(())", True),
    ("()()", True),
    ("((()))", True),
    ("(()())", True),
    (")(", False),
    (")(())", False),
    ("(()", False),
    ("())", False),
    ("(((", False),
    (")))", False),
    ("(()()", False),
    ("())(", False),
    ("()()()", True),
    ("((())())", True),
    ("(())(())", True),
    (")())", False),
    ("((())", False)
])
def test_correct_bracketing_parametrized(brackets, expected):
    assert correct_bracketing(brackets) == expected