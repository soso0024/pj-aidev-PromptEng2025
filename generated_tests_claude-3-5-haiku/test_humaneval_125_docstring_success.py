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

def test_split_words():
    assert split_words("Hello world!") == ["Hello", "world!"]
    assert split_words("Hello,world!") == ["Hello", "world!"]
    assert split_words("abcdef") == 3

def test_split_words_edge_cases():
    assert split_words("a,b,c") == ["a", "b", "c"]
    assert split_words("") == 0
    assert split_words("HELLO") == 0
    assert split_words("hello") == 3