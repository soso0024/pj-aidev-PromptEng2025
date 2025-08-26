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

def test_correct_bracketing_empty_string():
    assert correct_bracketing("") == True

def test_correct_bracketing_balanced_simple():
    assert correct_bracketing("<>") == True

def test_correct_bracketing_multiple_balanced():
    assert correct_bracketing("<<>>") == True
    assert correct_bracketing("<><>") == True

def test_correct_bracketing_unbalanced_negative():
    assert correct_bracketing(">") == False
    assert correct_bracketing("><<") == False

def test_correct_bracketing_unbalanced_positive():
    assert correct_bracketing("<") == False
    assert correct_bracketing("<<>") == False

def test_correct_bracketing_complex_cases():
    assert correct_bracketing("<<>><>") == True
    assert correct_bracketing("<<<>>>") == True
    assert correct_bracketing("<<>><<>>") == True

def test_correct_bracketing_invalid_cases():
    assert correct_bracketing("<>><") == False
    assert correct_bracketing("<<>><") == False
    assert correct_bracketing("><") == False

@pytest.mark.parametrize("input_str,expected", [
    ("", True),
    ("<>", True),
    ("<<>>", True),
    ("<><>", True),
    (">", False),
    ("<", False),
    ("<<>><>", True),
    ("<<<>>>", True),
    ("<>><", False),
    ("><", False)
])
def test_correct_bracketing_parametrized(input_str, expected):
    assert correct_bracketing(input_str) == expected
