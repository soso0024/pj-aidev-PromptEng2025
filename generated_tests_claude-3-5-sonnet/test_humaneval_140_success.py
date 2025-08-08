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
    ("hello world", "hello_world"),
    ("hello   world", "hello-world"),
    ("   ", "-"),
    ("", ""),
    ("a   b    c", "a-b-c"),
    ("test  string", "test__string"),
    ("no spaces", "no_spaces"),
    ("trailing   ", "trailing-"),
    ("   leading", "-leading"),
    ("mixed   spaces    here  now", "mixed-spaces-here__now"),
    ("a", "a"),
    ("  ", "_"),
    ("     ", "-"),
    ("a     b", "a-b"),
    ("multiple   spaces   between   words", "multiple-spaces-between-words"),
    ("single_char s    s", "single_char_s-s"),
    ("symbols#   @    !", "symbols#-@-!"),
    ("numbers 123   456    789", "numbers_123-456-789"),
    ("mix   of    different     spaces", "mix-of-different-spaces"),
    ("ends_with_three_spaces   ", "ends_with_three_spaces-")
])
def test_fix_spaces(text, expected):
    assert fix_spaces(text) == expected

def test_fix_spaces_empty_string():
    assert fix_spaces("") == ""

def test_fix_spaces_single_character():
    assert fix_spaces("x") == "x"

def test_fix_spaces_only_spaces():
    assert fix_spaces("     ") == "-"

def test_fix_spaces_alternating():
    assert fix_spaces("a b c d") == "a_b_c_d"

def test_fix_spaces_multiple_sections():
    assert fix_spaces("test   this    now  please") == "test-this-now__please"