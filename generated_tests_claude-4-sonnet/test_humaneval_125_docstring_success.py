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
        return len([i for i in txt if i.islower() and ord(i)%2 == 0])

@pytest.mark.parametrize("input_txt,expected", [
    ("Hello world!", ["Hello", "world!"]),
    ("Hello,world!", ["Hello", "world!"]),
    ("abcdef", 3),
    ("", 0),
    ("a", 0),
    ("b", 1),
    ("z", 1),
    ("y", 0),
    ("ABCDEF", 0),
    ("123456", 0),
    ("!@#$%^", 0),
    ("Hello world! How are you?", ["Hello", "world!", "How", "are", "you?"]),
    ("one,two,three,four", ["one", "two", "three", "four"]),
    ("a,b,c", ["a", "b", "c"]),
    ("word", 2),
    ("WORD", 0),
    ("Word", 2),
    ("a b c", ["a", "b", "c"]),
    ("a,b c", ["a,b", "c"]),
    ("   multiple   spaces   ", ["multiple", "spaces"]),
    (",,multiple,,commas,,", ["multiple", "commas"]),
    ("abcdefghijklmnopqrstuvwxyz", 13),
    ("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 0),
    ("aAbBcCdDeE", 2),
    ("13579", 0),
    ("a1b2c3", 1),
    ("hello world", ["hello", "world"]),
    ("hello,world", ["hello", "world"]),
    ("helloworld", 6),
    ("a c e g i k m o q s u w y", ["a", "c", "e", "g", "i", "k", "m", "o", "q", "s", "u", "w", "y"]),
    ("a,c,e,g,i,k,m,o,q,s,u,w,y", ["a", "c", "e", "g", "i", "k", "m", "o", "q", "s", "u", "w", "y"]),
    ("acegikmoqsuwy", 0),
    ("bdfhjlnprtvxz", 13),
])
def test_split_words(input_txt, expected):
    assert split_words(input_txt) == expected

def test_split_words_whitespace_priority():
    result = split_words("hello, world test")
    assert result == ["hello,", "world", "test"]

def test_split_words_comma_when_no_space():
    result = split_words("hello,world,test")
    assert result == ["hello", "world", "test"]

def test_split_words_count_lowercase_odd_positions():
    result = split_words("aceg")
    assert result == 0

def test_split_words_mixed_case_no_delimiters():
    result = split_words("AbCdEf")
    assert result == 3

def test_split_words_numbers_and_symbols():
    result = split_words("123!@#")
    assert result == 0

def test_split_words_single_character():
    assert split_words("a") == 0
    assert split_words("b") == 1
    assert split_words("A") == 0