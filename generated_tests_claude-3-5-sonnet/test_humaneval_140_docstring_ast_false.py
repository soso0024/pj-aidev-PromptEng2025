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
    ("Example", "Example"),
    ("Example 1", "Example_1"),
    (" Example 2", "_Example_2"),
    (" Example   3", "_Example-3"),
    ("   ", "-"),
    ("", ""),
    ("a b c", "a_b_c"),
    ("a   b    c", "a-b-c"),
    ("  a", "__a"),
    ("a  ", "a_"),
    ("a    ", "a-"),
    ("     test     ", "-test-"),
    ("Hello   World   Test", "Hello-World-Test"),
    ("a b  c   d    e", "a_b_c-d-e"),
    ("  multiple   spaces   here  ", "__multiple-spaces-here_"),
    ("no spaces", "no_spaces"),
    ("single space", "single_space"),
    ("triple   space", "triple-space"),
    ("ends with space ", "ends_with_space_"),
    ("     ", "-"),
])
def test_fix_spaces(text, expected):
    assert fix_spaces(text) == expected

def test_fix_spaces_empty_string():
    assert fix_spaces("") == ""

def test_fix_spaces_single_space():
    assert fix_spaces(" ") == "_"

def test_fix_spaces_only_spaces():
    assert fix_spaces("   ") == "-"
    assert fix_spaces("    ") == "-"
    assert fix_spaces("     ") == "-"

def test_fix_spaces_mixed_patterns():
    assert fix_spaces("a  b   c    d") == "a_b-c-d"
    assert fix_spaces(" a b c ") == "_a_b_c_"
    assert fix_spaces("  a   b    c  ") == "__a-b-c_"

def test_fix_spaces_special_characters():
    assert fix_spaces("hello world!") == "hello_world!"
    assert fix_spaces("hello   world!") == "hello-world!"
    assert fix_spaces("!@#   $%^") == "!@#-$%^"

def test_fix_spaces_numbers():
    assert fix_spaces("12 34 56") == "12_34_56"
    assert fix_spaces("12   34    56") == "12-34-56"

def test_fix_spaces_unicode():
    assert fix_spaces("über café") == "über_café"
    assert fix_spaces("über   café") == "über-café"