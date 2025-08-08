# Test cases for HumanEval/56
# Generated using Claude API



def correct_bracketing(brackets: str):
    """ brackets is a string of "<" and ">".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing("<")
    False
    >>> correct_bracketing("<>")
    True
    >>> correct_bracketing("<<><>>")
    True
    >>> correct_bracketing("><<>")
    False
    """

    depth = 0
    for b in brackets:
        if b == "<":
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
    assert correct_bracketing("<") == False

def test_single_closing_bracket():
    assert correct_bracketing(">") == False

def test_simple_valid_pair():
    assert correct_bracketing("<>") == True

@pytest.mark.parametrize("brackets,expected", [
    ("<>", True),
    ("<<>>", True),
    ("<<><>>", True),
    ("><", False),
    ("><<>", False),
    ("<<>", False),
    (">>>", False),
    ("<<<", False),
    ("<><><>", True),
    ("<<>><<>>", True),
    ("><><><><", False),
    ("", True),
    ("<<<<>>>>", True),
    ("><>><><>", False),
    ("<<>><><>", True)
])
def test_bracket_combinations(brackets, expected):
    assert correct_bracketing(brackets) == expected

def test_alternating_brackets():
    assert correct_bracketing("<><><><>") == True

def test_nested_brackets():
    assert correct_bracketing("<<<<<>>>>>") == True

def test_unbalanced_nested():
    assert correct_bracketing("<<<<<>>>>>>") == False

def test_closing_before_opening():
    assert correct_bracketing("><<><<") == False

def test_complex_valid_sequence():
    assert correct_bracketing("<><><<>><><>") == True

def test_complex_invalid_sequence():
    assert correct_bracketing("<><><<>><><>>") == False
