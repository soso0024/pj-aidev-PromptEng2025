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
    ("Hi", "Hi"),
    ("hello", "ehllo"),
    ("Hello World!!!", "Hello !!!Wdlor"),
    ("", ""),
    ("a", "a"),
    ("  ", "  "),
    ("abc def ghi", "abc def ghi"),
    ("zyxw vuts", "wxyz stuv"),
    ("123 abc", "123 abc"),
    ("!@#$ %^&*", "!#$@ %&*^"),
    ("aAaA bBbB", "AAaa BBbb"),
    ("Testing 123 Testing", "Teginst 123 Teginst"),
    ("   multiple   spaces   ", "   eillmptu   acepss   "),
    ("Python3.9", ".39Phnoty"),
    ("!@#$%^&*()", "!#$%&()*@^"),
    ("Mixed123Case", "123CMadeeisx"),
    ("a b c d e", "a b c d e"),
    ("zZ yY xX", "Zz Yy Xx")
])
def test_anti_shuffle_parametrized(input_str, expected):
    assert anti_shuffle(input_str) == expected

def test_anti_shuffle_empty():
    assert anti_shuffle("") == ""

def test_anti_shuffle_single_char():
    assert anti_shuffle("a") == "a"

def test_anti_shuffle_spaces():
    assert anti_shuffle("   ") == "   "

def test_anti_shuffle_special_chars():
    assert anti_shuffle("!@#$%") == "!#$%@"

def test_anti_shuffle_numbers():
    assert anti_shuffle("987654321") == "123456789"

def test_anti_shuffle_case_sensitivity():
    assert anti_shuffle("aBcDeF") == "BDFace"

def test_anti_shuffle_multiple_words():
    assert anti_shuffle("hello WORLD python") == "ehllo DLORW hnopty"

def test_anti_shuffle_mixed_content():
    assert anti_shuffle("Py123!@#thon") == "!#123@Phnoty"