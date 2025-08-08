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

def test_fix_spaces_empty_string():
    assert fix_spaces("") == ""

@pytest.mark.parametrize("input,expected", [
    ("hello world", "hello_world"),
    ("  hello   world  ", "_hello-world_"),
    ("one  two   three    four", "one_two-three-four"),
    ("   ", "_"),
    ("a b c", "a_b_c"),
    ("a   b   c", "a-b-c")
])
def test_fix_spaces_normal_cases(input, expected):
    assert fix_spaces(input) == expected

def test_fix_spaces_single_character():
    assert fix_spaces("a") == "a"

def test_fix_spaces_all_spaces():
    assert fix_spaces("   ") == "_"

def test_fix_spaces_leading_and_trailing_spaces():
    assert fix_spaces("  hello  ") == "_hello_"