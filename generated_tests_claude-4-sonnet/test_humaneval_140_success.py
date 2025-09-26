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

@pytest.mark.parametrize("input_text,expected", [
    ("", ""),
    ("a", "a"),
    ("hello", "hello"),
    ("a b", "a_b"),
    ("a  b", "a__b"),
    ("a   b", "a-b"),
    ("a    b", "a-b"),
    ("a     b", "a-b"),
    ("hello world", "hello_world"),
    ("hello  world", "hello__world"),
    ("hello   world", "hello-world"),
    ("hello    world", "hello-world"),
    ("a b c", "a_b_c"),
    ("a  b  c", "a__b__c"),
    ("a   b   c", "a-b-c"),
    ("a    b    c", "a-b-c"),
    ("a b  c   d", "a_b__c-d"),
    (" ", "_"),
    ("  ", "__"),
    ("   ", "-"),
    ("    ", "-"),
    ("     ", "-"),
    (" a", "_a"),
    ("  a", "__a"),
    ("   a", "-a"),
    ("    a", "-a"),
    ("a ", "a_"),
    ("a  ", "a__"),
    ("a   ", "a-"),
    ("a    ", "a-"),
    ("a     ", "a-"),
    (" a ", "_a_"),
    ("  a  ", "__a__"),
    ("   a   ", "-a-"),
    ("    a    ", "-a-"),
    ("ab cd ef", "ab_cd_ef"),
    ("ab  cd  ef", "ab__cd__ef"),
    ("ab   cd   ef", "ab-cd-ef"),
    ("test   with    multiple     spaces", "test-with-multiple-spaces"),
    ("single", "single"),
    ("no spaces here", "no_spaces_here"),
    ("multiple   different    space     counts", "multiple-different-space-counts"),
])
def test_fix_spaces_parametrized(input_text, expected):
    assert fix_spaces(input_text) == expected

def test_fix_spaces_empty_string():
    assert fix_spaces("") == ""

def test_fix_spaces_single_character():
    assert fix_spaces("x") == "x"

def test_fix_spaces_only_spaces():
    assert fix_spaces(" ") == "_"
    assert fix_spaces("  ") == "__"
    assert fix_spaces("   ") == "-"
    assert fix_spaces("    ") == "-"
    assert fix_spaces("     ") == "-"
    assert fix_spaces("      ") == "-"

def test_fix_spaces_leading_spaces():
    assert fix_spaces(" hello") == "_hello"
    assert fix_spaces("  hello") == "__hello"
    assert fix_spaces("   hello") == "-hello"
    assert fix_spaces("    hello") == "-hello"

def test_fix_spaces_trailing_spaces():
    assert fix_spaces("hello ") == "hello_"
    assert fix_spaces("hello  ") == "hello__"
    assert fix_spaces("hello   ") == "hello-"
    assert fix_spaces("hello    ") == "hello-"

def test_fix_spaces_mixed_patterns():
    assert fix_spaces("a b  c   d    e") == "a_b__c-d-e"
    assert fix_spaces(" a  b   c    ") == "_a__b-c-"
    assert fix_spaces("   start middle   end   ") == "-start_middle-end-"

def test_fix_spaces_no_spaces():
    assert fix_spaces("nospaces") == "nospaces"
    assert fix_spaces("alreadyprocessed") == "alreadyprocessed"

def test_fix_spaces_alternating_pattern():
    assert fix_spaces("a b a b a") == "a_b_a_b_a"
    assert fix_spaces("x  y  x  y") == "x__y__x__y"
    assert fix_spaces("m   n   m   n") == "m-n-m-n"