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

def split_words(txt):
    if " " in txt:
        return txt.split()
    elif "," in txt:
        return [x.strip() for x in txt.split(",")]
    else:
        return sum(1 for i in txt if i.islower() and ord(i) % 2 == 0)

def test_split_words_with_space():
    assert split_words("hello world") == ["hello", "world"]

def test_split_words_with_comma():
    assert split_words("apple,banana,cherry") == ["apple", "banana", "cherry"]

def test_split_words_with_no_space_or_comma():
    assert split_words("abcdefgh") == 4

def test_split_words_with_empty_string():
    assert split_words("") == 0

def test_split_words_with_non_alphabetic_characters():
    assert split_words("abc123def") == 3

@pytest.mark.parametrize("input,expected", [
    ("hello, world", ["hello", "world"]),
    ("apple,banana,cherry,", ["apple", "banana", "cherry"]),
    ("abcdefgh", 4),
    ("", 0),
    ("abc123def", 3)
])
def test_split_words_parametrized(input, expected):
    assert split_words(input) == expected