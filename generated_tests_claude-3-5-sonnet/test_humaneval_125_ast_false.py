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
    assert split_words("abcdefgh") == 4  # a, c, e, g are lowercase and odd ASCII
    assert split_words("ABCDEFGH") == 0  # no lowercase letters
    assert split_words("aeiou") == 3     # a, e, i, o, u - only a, i, u are odd ASCII

@pytest.mark.parametrize("input_str,expected", [
    ("hello world", ["hello", "world"]),
    ("a,b,c", ["a", "b", "c"]),
    ("abcdefgh", 4),
    ("UPPERCASE", 0),
    ("   multiple   spaces   ", ["multiple", "spaces"]),
    ("comma,separated,values", ["comma", "separated", "values"]),
    ("", 0),
    ("a", 0),
    ("bdfhjl", 3),
    ("zzz", 0)
])
def test_split_words_parametrized(input_str, expected):
    assert split_words(input_str) == expected

def test_split_words_empty_string():
    assert split_words("") == 0

def test_split_words_single_character():
    assert split_words("a") == 0
    assert split_words("b") == 0
    assert split_words("Z") == 0

def test_split_words_mixed_case():
    assert split_words("aBcDeFgH") == 2
    assert split_words("MiXeDcAsE") == 1

def test_split_words_special_characters():
    assert split_words("hello!world") == 3
    assert split_words("special@#$characters") == 4

def test_split_words_whitespace_variants():
    assert split_words("\t\ntest") == 1
    assert split_words("hello\tworld") == ["hello", "world"]
    assert split_words("hello\nworld") == ["hello", "world"]