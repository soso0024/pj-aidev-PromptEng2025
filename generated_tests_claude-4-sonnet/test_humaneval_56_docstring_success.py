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

def correct_bracketing(brackets: str):
    depth = 0
    for b in brackets:
        if b == "<":
            depth += 1
        else:
            depth -= 1
        if depth < 0:
            return False
    return depth == 0

def test_empty_string():
    assert correct_bracketing("") == True

def test_single_opening_bracket():
    assert correct_bracketing("<") == False

def test_single_closing_bracket():
    assert correct_bracketing(">") == False

def test_simple_pair():
    assert correct_bracketing("<>") == True

def test_multiple_pairs():
    assert correct_bracketing("<><>") == True

def test_nested_brackets():
    assert correct_bracketing("<<>>") == True

def test_complex_nested():
    assert correct_bracketing("<<><>>") == True

def test_closing_before_opening():
    assert correct_bracketing("><") == False

def test_closing_before_opening_complex():
    assert correct_bracketing("><<>") == False

def test_unmatched_opening():
    assert correct_bracketing("<<<>") == False

def test_unmatched_closing():
    assert correct_bracketing("<>>>") == False

def test_multiple_unmatched_opening():
    assert correct_bracketing("<<<<<") == False

def test_multiple_unmatched_closing():
    assert correct_bracketing(">>>>>") == False

def test_mixed_unmatched():
    assert correct_bracketing("<><><") == False

def test_deeply_nested():
    assert correct_bracketing("<<<>>>") == True

def test_very_deeply_nested():
    assert correct_bracketing("<<<<>>>>") == True

def test_alternating_pattern():
    assert correct_bracketing("<><><><>") == True

def test_complex_valid_pattern():
    assert correct_bracketing("<<><><>>") == True

def test_complex_invalid_pattern():
    assert correct_bracketing("<<>><>") == True

def test_starts_with_closing():
    assert correct_bracketing(">><<") == False

def test_ends_with_opening():
    assert correct_bracketing("<<>><<") == False

@pytest.mark.parametrize("brackets,expected", [
    ("", True),
    ("<", False),
    (">", False),
    ("<>", True),
    ("<<>>", True),
    ("><", False),
    ("<<<>>>", True),
    ("<<><>>", True),
    ("><<>", False),
    ("<><><>", True),
    (">>><<<", False),
    ("<<<<<>>>>>", True),
    ("><><><", False)
])
def test_parametrized_cases(brackets, expected):
    assert correct_bracketing(brackets) == expected
