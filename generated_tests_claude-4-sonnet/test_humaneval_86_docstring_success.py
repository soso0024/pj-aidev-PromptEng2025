# Test cases for HumanEval/86
# Generated using Claude API


def anti_shuffle(s):
    """
    Write a function that takes a string and returns an ordered version of it.
    Ordered version of string, is a string where all words (separated by space)
    are replaced by a new word where all the characters arranged in
    ascending order based on ascii value.
    Note: You should keep the order of words and blank spaces in the sentence.

    For example:
    anti_shuffle('Hi') returns 'Hi'
    anti_shuffle('hello') returns 'ehllo'
    anti_shuffle('Hello World!!!') returns 'Hello !!!Wdlor'
    """

    return ' '.join([''.join(sorted(list(i))) for i in s.split(' ')])


# Generated test cases:
import pytest

def anti_shuffle(s):
    return ' '.join([''.join(sorted(list(i))) for i in s.split(' ')])

@pytest.mark.parametrize("input_str,expected", [
    ("Hi", "Hi"),
    ("hello", "ehllo"),
    ("Hello World!!!", "Hello !!!Wdlor"),
    ("", ""),
    (" ", " "),
    ("  ", "  "),
    ("a", "a"),
    ("abc", "abc"),
    ("cba", "abc"),
    ("hello world", "ehllo dlorw"),
    ("The Quick Brown Fox", "Teh Qciku Bnorw Fox"),
    ("123", "123"),
    ("321", "123"),
    ("a1b2c3", "123abc"),
    ("!@#$%", "!#$%@"),
    ("Hello  World", "Hello  Wdlor"),
    ("  hello  world  ", "  ehllo  dlorw  "),
    ("single", "egilns"),
    ("UPPERCASE", "ACEEPPRSU"),
    ("MiXeD cAsE", "DMXei AEcs"),
    ("special!@#characters", "!#@aaaccceehilprrsst"),
    ("numbers123and456letters", "123456abdeeelmnnrrssttu"),
    ("tab\tspace", "\taabcepst"),
    ("newline\ntest", "\neeeilnnsttw")
])
def test_anti_shuffle_parametrized(input_str, expected):
    assert anti_shuffle(input_str) == expected

def test_anti_shuffle_empty_string():
    assert anti_shuffle("") == ""

def test_anti_shuffle_single_space():
    assert anti_shuffle(" ") == " "

def test_anti_shuffle_multiple_spaces():
    assert anti_shuffle("   ") == "   "

def test_anti_shuffle_single_character():
    assert anti_shuffle("a") == "a"

def test_anti_shuffle_already_sorted():
    assert anti_shuffle("abc def") == "abc def"

def test_anti_shuffle_reverse_sorted():
    assert anti_shuffle("zyx wvu") == "xyz uvw"

def test_anti_shuffle_mixed_case():
    assert anti_shuffle("ZaB") == "BZa"

def test_anti_shuffle_numbers_only():
    assert anti_shuffle("9876543210") == "0123456789"

def test_anti_shuffle_special_characters():
    assert anti_shuffle("!@# $%^") == "!#@ $%^"

def test_anti_shuffle_leading_trailing_spaces():
    assert anti_shuffle("  hello world  ") == "  ehllo dlorw  "

def test_anti_shuffle_multiple_consecutive_spaces():
    assert anti_shuffle("hello    world") == "ehllo    dlorw"

def test_anti_shuffle_unicode_characters():
    assert anti_shuffle("café") == "acfé"

def test_anti_shuffle_long_string():
    long_input = "abcdefghijklmnopqrstuvwxyz zyxwvutsrqponmlkjihgfedcba"
    expected = "abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz"
    assert anti_shuffle(long_input) == expected