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

def test_split_words_with_commas():
    assert split_words("Hello,world!") == ["Hello", "world!"]

def test_split_words_lowercase_odd_order():
    assert split_words("abcdef") == 3

def test_split_words_empty_string():
    assert split_words("") == 0

def test_split_words_only_uppercase():
    assert split_words("HELLO") == 0

def test_split_words_mixed_case():
    assert split_words("AbCdEf") == 3

def test_split_words_with_numbers():
    assert split_words("hello123world") == 3

def test_split_words_with_special_chars():
    assert split_words("a!b@c#d$e%f^") == 3

@pytest.mark.parametrize("input_str,expected", [
    ("Hello world!", ["Hello", "world!"]),
    ("Hello,world!", ["Hello", "world!"]),
    ("abcdef", 3),
    ("", 0),
    ("HELLO", 0),
    ("AbCdEf", 3),
    ("hello123world", 3),
    ("a!b@c#d$e%f^", 3)
])
def test_split_words_parametrized(input_str, expected):
    assert split_words(input_str) == expected