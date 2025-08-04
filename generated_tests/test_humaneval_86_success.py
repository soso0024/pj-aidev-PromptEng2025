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

@pytest.mark.parametrize("input_str,expected", [
    ("hello world", "ehllo dlorw"),
    ("python test", "hnopty estt"),
    ("", ""),
    ("a", "a"),
    ("abc def ghi", "abc def ghi"),
    ("zyxw vuts", "wxyz stuv"),
    ("  ", "  "),
    ("Hello World", "Hello Wdlor"),
    ("123 456", "123 456"),
    ("!@# $%^", "!#@ $%^"),
    ("aaa bbb ccc", "aaa bbb ccc"),
    ("zyx cba", "xyz abc"),
    ("a b c d e", "a b c d e"),
    ("   multiple   spaces   ", "   eillmptu   acepss   "),
    ("mix123 ed", "123imx de"),
])
def test_anti_shuffle(input_str, expected):
    assert anti_shuffle(input_str) == expected

def test_anti_shuffle_with_none():
    with pytest.raises(AttributeError):
        anti_shuffle(None)

def test_anti_shuffle_with_numbers():
    with pytest.raises(AttributeError):
        anti_shuffle(12345)

def test_anti_shuffle_with_special_chars():
    assert anti_shuffle("@#$ %^&") == "#$@ %&^"

def test_anti_shuffle_single_char_words():
    assert anti_shuffle("a b c") == "a b c"

def test_anti_shuffle_long_string():
    input_str = "pneumonoultramicroscopicsilicovolcanoconiosis supercalifragilisticexpialidocious"
    expected = "aacccccceiiiiiilllmmnnnnooooooooopprrsssstuuv aaacccdeefgiiiiiiillloopprrssstuux"
    assert anti_shuffle(input_str) == expected

def test_anti_shuffle_empty_string():
    assert anti_shuffle("") == ""

def test_anti_shuffle_whitespace():
    assert anti_shuffle("   ") == "   "

def test_anti_shuffle_mixed_case():
    assert anti_shuffle("HeLLo WoRLD") == "HLLeo DLRWo"