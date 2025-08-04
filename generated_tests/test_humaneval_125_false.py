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
    assert split_words("hello world") == ["hello", "world"]
    assert split_words("a b c") == ["a", "b", "c"]
    assert split_words("   multiple   spaces   ") == ["multiple", "spaces"]

def test_split_words_with_commas():
    assert split_words("hello,world") == ["hello", "world"]
    assert split_words("a,b,c") == ["a", "b", "c"]
    assert split_words("multiple,,commas") == ["multiple", "", "commas"]

def test_split_words_no_delimiter():
    assert split_words("abcdefgh") == 4  # a, c, e, g are lowercase and even ASCII
    assert split_words("UPPERCASE") == 0
    assert split_words("b") == 1  # b is lowercase and has odd ASCII value

@pytest.mark.parametrize("input_str,expected", [
    ("hello world", ["hello", "world"]),
    ("hello,world", ["hello", "world"]),
    ("abcdefgh", 4),
    ("", 0),
    ("   ", []),
    ("a,b,c", ["a", "b", "c"]),
    ("ABCDEF", 0),
    ("bdfhjl", 3),  # b, d, f, h, j, l are all odd ASCII values
    ("hello   world", ["hello", "world"]),
    ("hello,,,world", ["hello", "", "", "world"])
])
def test_split_words_parametrized(input_str, expected):
    assert split_words(input_str) == expected

def test_split_words_empty():
    assert split_words("") == 0

def test_split_words_whitespace():
    assert split_words("   ") == []

def test_split_words_mixed_case():
    assert split_words("aBcDeFgH") == 2  # Only counting lowercase letters with even ASCII values

def test_split_words_special_chars():
    assert split_words("!@#$%^") == 0

def test_split_words_numbers():
    assert split_words("123456") == 0

def test_split_words_mixed_content():
    assert split_words("Hello World 123") == ["Hello", "World", "123"]