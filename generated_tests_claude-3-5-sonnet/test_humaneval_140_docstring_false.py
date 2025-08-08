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
    ("", ""),
    (" ", "_"),
    ("  ", "_"),
    ("   ", "-"),
    ("    ", "-"),
    ("a b c", "a_b_c"),
    ("a   b   c", "a-b-c"),
    ("  end", "_end"),
    ("start  ", "start_"),
    ("start   ", "start-"),
    ("a  b   c    d", "a_b-c-d"),
    ("     multiple     spaces     ", "-multiple-spaces-"),
    ("no spaces", "no_spaces"),
    ("   leading", "-leading"),
    ("trailing   ", "trailing-"),
    ("mixed   spaces    and   gaps", "mixed-spaces-and-gaps"),
    ("a\tb\tc", "a\tb\tc"),
    ("  \t  ", "_\t_"),
    ("1 2 3", "1_2_3"),
    ("1   2   3", "1-2-3")
])
def test_fix_spaces_parametrized(text, expected):
    assert fix_spaces(text) == expected

def test_fix_spaces_none_input():
    with pytest.raises(TypeError):
        fix_spaces(None)

def test_fix_spaces_non_string_input():
    with pytest.raises(TypeError):
        fix_spaces(123)

def test_fix_spaces_special_characters():
    assert fix_spaces("hello!@#$%^&*() world") == "hello!@#$%^&*()_world"

def test_fix_spaces_unicode():
    assert fix_spaces("héllo   wórld") == "héllo-wórld"

def test_fix_spaces_newlines():
    assert fix_spaces("hello\n   world") == "hello\n-world"

def test_fix_spaces_multiple_lines():
    assert fix_spaces("line1\n   line2\n  line3") == "line1\n-line2\n_line3"