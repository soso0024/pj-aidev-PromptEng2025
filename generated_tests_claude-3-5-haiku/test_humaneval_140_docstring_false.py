# Test cases for HumanEval/140
# Generated using Claude API


def fix_spaces(text):
    """
    Given a string text, replace all spaces in it with underscores, 
    and if a string has more than 2 consecutive spaces, 
    then replace all consecutive spaces with - 
    
    fix_spaces("Example") == "Example"
    fix_spaces("Example 1") == "Example_1"
    fix_spaces(" Example 2") == "_Example_2"
    fix_spaces(" Example   3") == "_Example-3"
    """

    new_text = ""
    i = 0
    start, end = 0, 0
    while i < len(text):
        if text[i] == " ":
            end += 1
        else:
            if end - start > 2:
                new_text += "-"+text[i]
            elif end - start > 0:
                new_text += "_"*(end - start)+text[i]
            else:
                new_text += text[i]
            start, end = i+1, i+1
        i+=1
    if end - start > 2:
        new_text += "-"
    elif end - start > 0:
        new_text += "_"
    return new_text


# Generated test cases:
import pytest

def test_fix_spaces_no_spaces():
    assert fix_spaces("Example") == "Example"

def test_fix_spaces_single_space():
    assert fix_spaces("Example 1") == "Example_1"

def test_fix_spaces_leading_space():
    assert fix_spaces(" Example 2") == "_Example_2"

def test_fix_spaces_multiple_consecutive_spaces():
    assert fix_spaces(" Example   3") == "_Example-3"

def test_fix_spaces_multiple_spaces_at_end():
    assert fix_spaces("Test    ") == "Test-"

def test_fix_spaces_multiple_spaces_at_start():
    assert fix_spaces("    Test") == "-Test"

def test_fix_spaces_empty_string():
    assert fix_spaces("") == ""

@pytest.mark.parametrize("input_text,expected", [
    ("Hello World", "Hello_World"),
    ("  Multiple   Spaces  ", "-Multiple-Spaces-"),
    ("No Change", "No_Change"),
    ("   ", "-"),
    ("Trailing Spaces   ", "Trailing_Spaces-")
])
def test_fix_spaces_parametrized(input_text, expected):
    assert fix_spaces(input_text) == expected