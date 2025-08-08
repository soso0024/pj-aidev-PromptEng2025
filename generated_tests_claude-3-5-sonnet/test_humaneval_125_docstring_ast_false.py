# Test cases for HumanEval/125
# Generated using Claude API


def split_words(txt):
    '''
    Given a string of words, return a list of words split on whitespace, if no whitespaces exists in the text you
    should split on commas ',' if no commas exists you should return the number of lower-case letters with odd order in the
    alphabet, ord('a') = 0, ord('b') = 1, ... ord('z') = 25
    Examples
    split_words("Hello world!") ➞ ["Hello", "world!"]
    split_words("Hello,world!") ➞ ["Hello", "world!"]
    split_words("abcdef") == 3 
    '''

    if " " in txt:
        return txt.split()
    elif "," in txt:
        return txt.replace(',',' ').split()
    else:
        return len([i for i in txt if i.islower() and ord(i)%2 == 0])


# Generated test cases:
import pytest

def test_split_words_with_spaces():
    assert split_words("Hello world!") == ["Hello", "world!"]
    assert split_words("Python is awesome") == ["Python", "is", "awesome"]
    assert split_words(" leading space") == ["leading", "space"]
    assert split_words("trailing space ") == ["trailing", "space"]
    assert split_words("   multiple   spaces   ") == ["multiple", "spaces"]

def test_split_words_with_commas():
    assert split_words("Hello,world!") == ["Hello", "world!"]
    assert split_words("a,b,c") == ["a", "b", "c"]
    assert split_words(",leading,comma") == ["", "leading", "comma"]
    assert split_words("trailing,comma,") == ["trailing", "comma", ""]

def test_split_words_count_lowercase():
    assert split_words("abcdef") == 3  # b, d, f are even positions
    assert split_words("xyz") == 2      # y and z are even positions
    assert split_words("UPPERCASE") == 0
    assert split_words("") == 0
    assert split_words("aaa") == 0      # a is position 0 (odd)

@pytest.mark.parametrize("input_str,expected", [
    ("Hello world!", ["Hello", "world!"]),
    ("Hello,world!", ["Hello", "world!"]),
    ("abcdef", 3),
    ("", 0),
    ("   ", []),
    ("a,b,c", ["a", "b", "c"]),
    ("ABCDEF", 0),
    ("a b,c", ["a", "b,c"]),
    ("xyz", 2),
    ("!@#$%^", 0)
])
def test_split_words_parametrized(input_str, expected):
    assert split_words(input_str) == expected

def test_split_words_mixed_case():
    assert split_words("aBcDeF") == 0  # only counting lowercase letters
    assert split_words("MiXeDcAsE") == 0

def test_split_words_special_characters():
    assert split_words("!@#$%^") == 0
    assert split_words("a!b@c#") == 1  # only b is in even position

def test_split_words_numbers():
    assert split_words("123") == 0
    assert split_words("a1b2c3") == 1  # only b is in even position

def test_split_words_whitespace_variants():
    assert split_words("Tab Separated") == ["Tab", "Separated"]
    assert split_words("Newline Separated") == ["Newline", "Separated"]
    assert split_words("Carriage Return") == ["Carriage", "Return"]