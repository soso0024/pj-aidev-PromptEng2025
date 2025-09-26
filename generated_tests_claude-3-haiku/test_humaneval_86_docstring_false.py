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
from functools import reduce

def test_anti_shuffle(s, expected):
    assert anti_shuffle(s) == expected

def test_anti_shuffle_empty_string():
    assert anti_shuffle("") == ""

def test_anti_shuffle_single_character():
    assert anti_shuffle("a") == "a"

def test_anti_shuffle_all_whitespace():
    assert anti_shuffle("   ") == "   "

def test_anti_shuffle_all_punctuation():
    assert anti_shuffle("!@#$%^&*()") == "!#$%&*()@^"

def test_anti_shuffle_mixed_case():
    assert anti_shuffle("Hello World") == "Hello Wdlor"

def test_anti_shuffle_numbers():
    assert anti_shuffle("123 456 789") == "123 456 789"

def test_anti_shuffle_leading_trailing_spaces():
    assert anti_shuffle("  Hello World  ") == "  Hello Wdlor  "

def test_anti_shuffle_multiple_spaces():
    assert anti_shuffle("Hello   World") == "Hello   Wdlor"