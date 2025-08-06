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

def test_basic_word():
    assert anti_shuffle("hello") == "ehllo"

def test_multiple_words():
    assert anti_shuffle("hello world") == "ehllo dlorw"

def test_empty_string():
    assert anti_shuffle("") == ""

def test_single_character():
    assert anti_shuffle("a") == "a"

def test_numbers_and_special_chars():
    assert anti_shuffle("12345 !@#$%") == "12345 !#$%@"

@pytest.mark.parametrize("input_str,expected", [
    ("python programming", "hnopty aggimmnoprr"),
    ("   ", "   "),
    ("a b c", "a b c"),
    ("zyxw vuts", "wxyz stuv"),
    ("Hello World", "Hello Wdlor"),
    ("123 abc", "123 abc"),
    ("!@#$ %^&*", "!#$@ %&*^"),
    ("aAaA bBbB", "AAAa BBbb"),
])
def test_various_inputs(input_str, expected):
    assert anti_shuffle(input_str) == expected

def test_multiple_spaces():
    assert anti_shuffle("word   another") == "dorw   aehnort"

def test_special_whitespace():
    assert anti_shuffle("word\tword") == "\tddoorrww"

def test_unicode_characters():
    assert anti_shuffle("über café") == "berü acfé"

def test_mixed_case():
    assert anti_shuffle("HeLLo WoRLD") == "HLLeo DLRWo"

def test_repeated_characters():
    assert anti_shuffle("aaa bbb") == "aaa bbb"

def test_single_space():
    assert anti_shuffle(" ") == " "

def test_leading_trailing_spaces():
    assert anti_shuffle("  hello  world  ") == "  ehllo  dlorw  "