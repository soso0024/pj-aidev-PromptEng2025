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
        return [i for i in txt if i.islower() and ord(i)%2 == 0]

def test_split_words_with_space():
    assert split_words("hello world") == ["hello", "world"]

def test_split_words_with_comma():
    assert split_words("apple,banana,cherry") == ["apple", "banana", "cherry"]

def test_split_words_no_space_or_comma():
    assert len(split_words("abcdefgh")) == 4

def test_split_words_empty_string():
    assert split_words("") == []

@pytest.mark.parametrize("input,expected", [
    ("  leading/trailing spaces  ", ["leading/trailing", "spaces"]),
    ("multiple,commas,in,a,row", ["multiple", "commas", "in", "a", "row"]),
    ("all lowercase even chars", 8),
    ("MixedCase", 1),
    ("1234567890", 0)
])
def test_split_words_edge_cases(input, expected):
    assert split_words(input) == expected

def test_split_words_type_error():
    with pytest.raises(TypeError):
        split_words(123)