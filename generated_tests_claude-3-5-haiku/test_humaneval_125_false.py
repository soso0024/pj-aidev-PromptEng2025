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

def test_split_words_space_separated():
    assert split_words("hello world") == ["hello", "world"]

def test_split_words_comma_separated():
    assert split_words("hello,world") == ["hello", "world"]

def test_split_words_single_word():
    assert split_words("hello") == 3

def test_split_words_empty_string():
    assert split_words("") == 0

def test_split_words_multiple_spaces():
    assert split_words("hello   world") == ["hello", "world"]

def test_split_words_mixed_separators():
    assert split_words("hello, world") == ["hello", "world"]

@pytest.mark.parametrize("input_text,expected", [
    ("hello world", ["hello", "world"]),
    ("hello,world", ["hello", "world"]),
    ("abcdefg", 3),
    ("", 0),
    ("HELLO WORLD", []),
    ("hello, world", ["hello", "world"])
])
def test_split_words_parametrized(input_text, expected):
    assert split_words(input_text) == expected