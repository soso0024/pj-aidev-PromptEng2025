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
        return txt.replace(',',' ').split()
    else:
        return len([i for i in txt if i.islower() and (ord(i) - ord('a')) % 2 == 1])

def test_split_words_with_spaces():
    assert split_words("Hello world!") == ["Hello", "world!"]

def test_split_words_with_commas():
    assert split_words("Hello,world!") == ["Hello", "world!"]

def test_split_words_lowercase_odd_order():
    assert split_words("abcdef") == 3

def test_split_words_empty_string():
    assert split_words("") == 0

def test_split_words_only_uppercase():
    assert split_words("ABCDEF") == 0

def test_split_words_mixed_case():
    assert split_words("AbCdEf") == 3

def test_split_words_with_multiple_spaces():
    assert split_words("Hello   world  test") == ["Hello", "world", "test"]

def test_split_words_with_multiple_commas():
    assert split_words("Hello,world,test") == ["Hello", "world", "test"]

@pytest.mark.parametrize("input_str,expected", [
    ("Hello world!", ["Hello", "world!"]),
    ("Hello,world!", ["Hello", "world!"]),
    ("abcdef", 3),
    ("", 0),
    ("ABCDEF", 0),
    ("AbCdEf", 3),
    ("Hello   world  test", ["Hello", "world", "test"]),
    ("Hello,world,test", ["Hello", "world", "test"])
])
def test_split_words_parametrized(input_str, expected):
    assert split_words(input_str) == expected