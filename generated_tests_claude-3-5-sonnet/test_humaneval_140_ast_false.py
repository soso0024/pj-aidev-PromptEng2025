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

@pytest.mark.parametrize("text,expected", [
    ("hello", "hello"),
    ("hello world", "hello_world"),
    ("hello  world", "hello__world"),
    ("hello   world", "hello-world"),
    ("hello    world", "hello-world"),
    ("a   b   c", "a-b-c"),
    ("", ""),
    (" ", "_"),
    ("  ", "__"),
    ("   ", "-"),
    ("    ", "-"),
    ("a ", "a_"),
    ("a  ", "a__"),
    ("a   ", "a-"),
    (" a", "_a"),
    ("  a", "__a"),
    ("   a", "-a"),
    ("a b c", "a_b_c"),
    ("a  b  c", "a__b__c"),
    ("text   with   multiple   spaces", "text-with-multiple-spaces"),
    ("ends   ", "ends-"),
    ("   starts", "-starts"),
    ("mixed   spaces  and single spaces", "mixed-spaces__and_single_spaces"),
    ("a\tb", "a\tb"),
    ("a\nb", "a\nb"),
])
def test_fix_spaces(text, expected):
    assert fix_spaces(text) == expected

def test_fix_spaces_empty():
    assert fix_spaces("") == ""

def test_fix_spaces_single_char():
    assert fix_spaces("a") == "a"

def test_fix_spaces_only_spaces():
    assert fix_spaces("     ") == "-"

def test_fix_spaces_multiple_sections():
    assert fix_spaces("one   two    three   four") == "one-two-three-four"

def test_fix_spaces_edge_spaces():
    assert fix_spaces("   text   ") == "-text-"

def test_fix_spaces_alternating():
    assert fix_spaces("a b c   d e   f g") == "a_b_c-d_e-f_g"