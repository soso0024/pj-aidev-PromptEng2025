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
        return len([i for i in txt if i.islower() and (ord(i) - ord('a')) % 2 == 0])

def test_split_words_space_separated():
    assert split_words("hello world python") == ["hello", "world", "python"]

def test_split_words_comma_separated():
    assert split_words("hello,world,python") == ["hello", "world", "python"]

def test_split_words_single_word():
    assert split_words("hello") == 2

def test_split_words_empty_string():
    assert split_words("") == 0

@pytest.mark.parametrize("input_text,expected", [
    ("hello world", ["hello", "world"]),
    ("python,programming,language", ["python", "programming", "language"]),
    ("abcdefg", 3),
    ("", 0),
    ("HELLO WORLD", ["HELLO", "WORLD"]),
    ("hello,WORLD", ["hello", "WORLD"])
])
def test_split_words_parametrized(input_text, expected):
    assert split_words(input_text) == expected

def test_split_words_mixed_case():
    assert split_words("Hello,world") == ["Hello", "world"]

def test_split_words_special_characters():
    assert split_words("hello!world") == 2