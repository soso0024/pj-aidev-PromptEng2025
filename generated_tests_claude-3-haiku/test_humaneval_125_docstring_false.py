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

@pytest.mark.parametrize("input,expected", [
    ("Hello world!", ["Hello", "world!"]),
    ("Hello,world!", ["Hello", "world!"]),
    ("abcdef", 3),
    ("  Hello   world  ", ["Hello", "world"]),
    ("", 0),
    ("ABC", 0),
    ("aBcD", 2),
    ("a,b,c,d", ["a", "b", "c", "d"]),
    ("   ", 0),
    (None, TypeError),
])
def test_split_words(input, expected):
    if isinstance(expected, type):
        with pytest.raises(expected):
            split_words(input)
    else:
        assert split_words(input) == expected