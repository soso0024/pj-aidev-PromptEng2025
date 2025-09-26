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

def test_split_words_with_spaces():
    assert split_words("hello world") == ["hello", "world"]
    assert split_words("one two three") == ["one", "two", "three"]
    assert split_words("a b c d e") == ["a", "b", "c", "d", "e"]
    assert split_words("  multiple   spaces  ") == ["multiple", "spaces"]
    assert split_words(" leading space") == ["leading", "space"]
    assert split_words("trailing space ") == ["trailing", "space"]

def test_split_words_with_commas():
    assert split_words("hello,world") == ["hello", "world"]
    assert split_words("one,two,three") == ["one", "two", "three"]
    assert split_words("a,b,c,d,e") == ["a", "b", "c", "d", "e"]
    assert split_words("hello,,world") == ["hello", "", "world"]
    assert split_words(",leading,comma") == ["", "leading", "comma"]
    assert split_words("trailing,comma,") == ["trailing", "comma", ""]

def test_split_words_with_commas_and_spaces():
    assert split_words("hello, world") == ["hello,", "world"]
    assert split_words("one, two, three") == ["one,", "two,", "three"]

def test_split_words_count_lowercase_even_ord():
    assert split_words("abcd") == 2
    assert split_words("ABCD") == 0
    assert split_words("AbCd") == 2
    assert split_words("bdfhjlnprtvxz") == 13
    assert split_words("acegikmoqsuwy") == 0

def test_split_words_empty_string():
    assert split_words("") == 0

def test_split_words_single_space():
    assert split_words(" ") == []

def test_split_words_single_comma():
    assert split_words(",") == ["", ""]

def test_split_words_mixed_case_no_delimiters():
    assert split_words("AbCdEfGh") == 4
    assert split_words("HELLO") == 0
    assert split_words("hello") == 3

def test_split_words_numbers_and_symbols():
    assert split_words("123456") == 0
    assert split_words("!@#$%^") == 0
    assert split_words("a1b2c3") == 1

def test_split_words_unicode_characters():
    assert split_words("αβγδ") == 2
    assert split_words("café") == 1

@pytest.mark.parametrize("input_text,expected", [
    ("hello world", ["hello", "world"]),
    ("a,b,c", ["a", "b", "c"]),
    ("abcd", 2),
    ("", 0),
    ("HELLO", 0),
    ("bdfh", 4),
    ("aceg", 0),
    ("Hello World", ["Hello", "World"]),
    ("test,case", ["test", "case"]),
    ("MixedCase", 2)
])
def test_split_words_parametrized(input_text, expected):
    assert split_words(input_text) == expected