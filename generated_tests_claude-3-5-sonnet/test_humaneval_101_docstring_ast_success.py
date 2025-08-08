# Test cases for HumanEval/101
# Generated using Claude API


def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    """

    if not s:
        return []

    s_list = []

    for letter in s:
        if letter == ',':
            s_list.append(' ')
        else:
            s_list.append(letter)

    s_list = "".join(s_list)
    return s_list.split()


# Generated test cases:
import pytest

def test_words_string_basic():
    assert words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    assert words_string("One, two, three") == ["One", "two", "three"]

@pytest.mark.parametrize("input_str,expected", [
    ("", []),
    ("Single", ["Single"]),
    ("Hello World", ["Hello", "World"]),
    ("One,two,three", ["One", "two", "three"]),
    ("Multiple   spaces   here", ["Multiple", "spaces", "here"]),
    ("Comma, with, spaces", ["Comma", "with", "spaces"]),
    ("Mix,of spaces,and,commas here", ["Mix", "of", "spaces", "and", "commas", "here"]),
    ("   Leading spaces", ["Leading", "spaces"]),
    ("Trailing spaces   ", ["Trailing", "spaces"]),
    (",,,", []),
    ("   ", []),
    ("Word,,,word", ["Word", "word"]),
    ("Hello,,,,World", ["Hello", "World"]),
    ("Special!@#$%^&*, chars", ["Special!@#$%^&*", "chars"])
])
def test_words_string_parametrized(input_str, expected):
    assert words_string(input_str) == expected

def test_words_string_with_numbers():
    assert words_string("1, 2, 3, 4") == ["1", "2", "3", "4"]
    assert words_string("Mix 123, 456 numbers") == ["Mix", "123", "456", "numbers"]

def test_words_string_unicode():
    assert words_string("Hello, 世界") == ["Hello", "世界"]
    assert words_string("über, café") == ["über", "café"]

def test_words_string_with_tabs():
    assert words_string("Word\tword,word") == ["Word", "word", "word"]
    assert words_string("\tLeading\tTab") == ["Leading", "Tab"]
