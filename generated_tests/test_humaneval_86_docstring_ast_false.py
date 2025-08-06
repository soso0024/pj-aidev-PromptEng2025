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

def test_empty_string():
    assert anti_shuffle("") == ""

def test_single_word():
    assert anti_shuffle("hello") == "ehllo"
    assert anti_shuffle("python") == "hnopty"
    assert anti_shuffle("aaa") == "aaa"

def test_multiple_words():
    assert anti_shuffle("hello world") == "ehllo dlorw"
    assert anti_shuffle("python is awesome") == "hnopty is aeemosw"

def test_special_characters():
    assert anti_shuffle("Hello World!!!") == "Hello !!!Wdlor"
    assert anti_shuffle("a!b@c#d$") == "!#$@abcd"

def test_numbers():
    assert anti_shuffle("123 456") == "123 456"
    assert anti_shuffle("ab12 cd34") == "12ab 34cd"

def test_multiple_spaces():
    assert anti_shuffle("hello   world") == "ehllo   dlorw"
    assert anti_shuffle("  spaces  here  ") == "  acepss  eehr  "

@pytest.mark.parametrize("input_str,expected", [
    ("Hello", "Hello"),
    ("ZYX ABC", "XYZ ABC"),
    ("!@#$%", "!#$%@"),
    ("12321", "12233"),
    ("a b c", "a b c"),
    ("Testing 123", "Teginsst 123"),
    ("   ", "   "),
    ("a", "a"),
    ("aA bB cC", "aA bB cC"),
    ("Python3.9", ".39Phnoty")
])
def test_parametrized_cases(input_str, expected):
    assert anti_shuffle(input_str) == expected

def test_case_sensitivity():
    assert anti_shuffle("aBcDeF") == "aBcDeF"
    assert anti_shuffle("HELLO world") == "EHLLO dlorw"

def test_whitespace_preservation():
    assert anti_shuffle("\t\ntest") == "\t\nestt"
    assert anti_shuffle("word\n") == "dorw\n"

def test_unicode_characters():
    assert anti_shuffle("über café") == "berü acéf"
    assert anti_shuffle("こんにちは") == "こちにはん"