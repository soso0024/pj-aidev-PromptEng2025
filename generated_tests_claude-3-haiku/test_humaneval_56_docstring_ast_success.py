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

@pytest.mark.parametrize("brackets, expected", [
    ("<", False),
    ("<>", True),
    ("<<><>>", True),
    ("><<>", False),
    ("", True),
    ("<<<<", False),
    (">>>>", False),
    ("<><><>", True),
    ("<<>>", True),
    ("><", False),
])
def test_correct_bracketing(brackets, expected):
    assert correct_bracketing(brackets) == expected

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
