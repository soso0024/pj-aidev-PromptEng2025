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
        new_text += "_"*(end - start)
    return new_text

@pytest.mark.parametrize("text,expected", [
    ("Example", "Example"),
    ("Example 1", "Example_1"),
    (" Example 2", "_Example_2"),
    (" Example   3", "_Example-3"),
    ("", ""),
    (" ", "_"),
    ("  ", "__"),
    ("   ", "-"),
    ("    ", "-"),
    ("     ", "-"),
    ("a b", "a_b"),
    ("a  b", "a__b"),
    ("a   b", "a-b"),
    ("a    b", "a-b"),
    ("a     b", "a-b"),
    ("   a", "-a"),
    ("    a", "-a"),
    ("a   ", "a-"),
    ("a    ", "a-"),
    ("hello world", "hello_world"),
    ("hello  world", "hello__world"),
    ("hello   world", "hello-world"),
    ("hello    world", "hello-world"),
    ("   hello   world   ", "-hello-world-"),
    ("a b c", "a_b_c"),
    ("a  b  c", "a__b__c"),
    ("a   b   c", "a-b-c"),
    ("a    b    c", "a-b-c"),
    ("test   with    multiple     spaces", "test-with-multiple-spaces"),
    ("no spaces", "no_spaces"),
    ("multiple   consecutive    groups     here", "multiple-consecutive-groups-here"),
    ("x", "x"),
    ("x ", "x_"),
    ("x  ", "x__"),
    ("x   ", "x-"),
    (" x", "_x"),
    ("  x", "__x"),
    ("   x", "-x"),
    ("a b  c   d    e", "a_b__c-d-e"),
])
def test_fix_spaces(text, expected):
    assert fix_spaces(text) == expected

def test_fix_spaces_single_character():
    assert fix_spaces("a") == "a"

def test_fix_spaces_only_spaces():
    assert fix_spaces("   ") == "-"
    assert fix_spaces("    ") == "-"
    assert fix_spaces("     ") == "-"

def test_fix_spaces_mixed_patterns():
    assert fix_spaces("a b  c   d") == "a_b__c-d"
    assert fix_spaces("  a   b  ") == "__a-b__"

def test_fix_spaces_edge_cases():
    assert fix_spaces("") == ""
    assert fix_spaces("abc") == "abc"
    assert fix_spaces(" a b c ") == "_a_b_c_"