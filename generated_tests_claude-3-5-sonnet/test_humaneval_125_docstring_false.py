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

@pytest.mark.parametrize("input_str,expected", [
    ("Hello world!", ["Hello", "world!"]),
    ("Hello,world!", ["Hello", "world!"]),
    ("Hello, world!", ["Hello", "world!"]),
    ("abcdef", 3),
    ("", 0),
    ("ABCDEF", 0),
    ("a b c", ["a", "b", "c"]),
    ("a,b,c", ["a", "b", "c"]),
    ("aeiou", 2),
    ("xyz", 1),
    ("Hello World Hello", ["Hello", "World", "Hello"]),
    ("Hello,World,Hello", ["Hello", "World", "Hello"]),
    ("123", 0),
    ("!@#$%", 0),
    ("aBcDeF", 3),
    ("a,b c", ["a,b", "c"]),
    ("   spaces   ", ["spaces"]),
    ("no,extra,,spaces", ["no", "extra", "spaces"]),
    ("mixed,CASE,text", ["mixed", "CASE", "text"]),
    ("bdfhjl", 3)
])
def test_split_words(input_str, expected):
    assert split_words(input_str) == expected

def test_split_words_empty():
    assert split_words("") == 0

def test_split_words_single_char():
    assert split_words("a") == 1
    assert split_words("z") == 1

def test_split_words_special_chars():
    assert split_words("!@#") == 0
    assert split_words(".,;") == 0

def test_split_words_multiple_spaces():
    assert split_words("word   another    word") == ["word", "another", "word"]

def test_split_words_multiple_commas():
    assert split_words("word,,another,,,word") == ["word", "another", "word"]

def test_split_words_mixed_case():
    assert split_words("aBcDeFgHiJkLmNoPqRsTuVwXyZ") == 3

def test_split_words_numbers():
    assert split_words("123abc456") == 1

def test_split_words_whitespace_priority():
    assert split_words("Hello,world world") == ["Hello,world", "world"]