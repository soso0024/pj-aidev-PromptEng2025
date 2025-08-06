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

@pytest.mark.parametrize("brackets,expected", [
    ("", True),
    ("<>", True),
    ("<<>>", True),
    ("<><>", True),
    ("<<><>>", True),
    ("><", False),
    ("<", False),
    (">", False),
    ("<<>", False),
    ("<>>", False),
    (">>>", False),
    ("<<<", False),
    ("<>><", False),
    ("<><><><><>", True),
    ("<<<<<>>>>>", True),
    ("><><><><><", False),
    ("", True),
    ("<<<<>>>>", True),
    ("<<>><<>>", True),
    ("<<>><><>", True),
    ("><><><><", False),
    (">><<", False),
    (">>><<<", False),
])
def test_correct_bracketing(brackets, expected):
    assert correct_bracketing(brackets) == expected

def test_correct_bracketing_empty_string():
    assert correct_bracketing("") == True

def test_correct_bracketing_single_pair():
    assert correct_bracketing("<>") == True

def test_correct_bracketing_nested():
    assert correct_bracketing("<<>>") == True

def test_correct_bracketing_multiple_pairs():
    assert correct_bracketing("<><><>") == True

def test_correct_bracketing_invalid_start():
    assert correct_bracketing("><") == False

def test_correct_bracketing_unclosed():
    assert correct_bracketing("<") == False

def test_correct_bracketing_unopened():
    assert correct_bracketing(">") == False

def test_correct_bracketing_complex_valid():
    assert correct_bracketing("<<>><><>") == True

def test_correct_bracketing_complex_invalid():
    assert correct_bracketing("<<>>><") == False
