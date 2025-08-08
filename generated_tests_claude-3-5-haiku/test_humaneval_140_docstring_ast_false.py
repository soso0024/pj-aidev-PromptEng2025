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

def fix_spaces(text):
    new_text = ""
    i = 0
    start, end = 0, 0
    while i < len(text):
        if text[i] == " " or text[i] == "\t":
            end += 1
        else:
            if end - start > 2:
                new_text += "-" + text[i]
            elif end - start > 0:
                new_text += "_" * (end - start) + text[i]
            else:
                new_text += text[i]
            start, end = i+1, i+1
        i += 1
    
    if end - start > 2:
        new_text += "-"
    elif end - start > 0:
        new_text += "_"
    
    if len(text) > 0 and (text[0] == " " or text[0] == "\t"):
        new_text = "_" + new_text
    
    if len(text) > 0 and (text[-1] == " " or text[-1] == "\t"):
        new_text += "_"
    
    return new_text

def test_fix_spaces_basic_cases():
    assert fix_spaces("Example") == "Example"
    assert fix_spaces("Example 1") == "Example_1"
    assert fix_spaces(" Example 2") == "_Example_2"
    assert fix_spaces(" Example   3") == "_Example-3"

@pytest.mark.parametrize("input_text,expected", [
    ("", ""),
    ("NoSpaces", "NoSpaces"),
    ("Single Space", "Single_Space"),
    ("  Multiple  Spaces  ", "_Multiple-Spaces-"),
    ("Leading Spaces", "_Leading_Spaces"),
    ("Trailing Spaces   ", "Trailing_Spaces-"),
    ("   Multiple   Consecutive   Spaces   ", "_Multiple-Consecutive-Spaces-")
])
def test_fix_spaces_parametrized(input_text, expected):
    assert fix_spaces(input_text) == expected

def test_fix_spaces_edge_cases():
    assert fix_spaces("   ") == "-"
    assert fix_spaces("    ") == "-"
    assert fix_spaces(" a ") == "_a_"
    assert fix_spaces("a   b") == "a-b"

def test_fix_spaces_unicode():
    assert fix_spaces("Hello World") == "Hello_World"
    assert fix_spaces("こんにちは 世界") == "こんにちは_世界"

def test_fix_spaces_mixed_whitespace():
    assert fix_spaces("Mixed   \t  Spaces") == "Mixed-Spaces"