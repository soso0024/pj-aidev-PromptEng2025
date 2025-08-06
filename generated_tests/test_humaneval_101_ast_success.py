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

def test_empty_string():
    assert words_string("") == []

def test_single_word():
    assert words_string("hello") == ["hello"]

def test_multiple_words():
    assert words_string("hello world") == ["hello", "world"]

def test_comma_separation():
    assert words_string("hello,world") == ["hello", "world"]

def test_multiple_commas():
    assert words_string("one,two,three") == ["one", "two", "three"]

def test_spaces_and_commas():
    assert words_string("hello, world") == ["hello", "world"]

def test_multiple_spaces():
    assert words_string("hello   world") == ["hello", "world"]

def test_leading_trailing_spaces():
    assert words_string("  hello world  ") == ["hello", "world"]

@pytest.mark.parametrize("input_str,expected", [
    ("hello,world", ["hello", "world"]),
    ("one,two,three", ["one", "two", "three"]),
    ("hello world", ["hello", "world"]),
    ("", []),
    ("single", ["single"]),
    ("  spaces  between  ", ["spaces", "between"]),
    ("comma,with, spaces", ["comma", "with", "spaces"]),
    ("multiple,,,commas", ["multiple", "commas"]),
])
def test_words_string_parametrized(input_str, expected):
    assert words_string(input_str) == expected

def test_special_characters():
    assert words_string("hello!,world?") == ["hello!", "world?"]

def test_numbers():
    assert words_string("123,456 789") == ["123", "456", "789"]

def test_mixed_content():
    assert words_string("Hello123,World!456") == ["Hello123", "World!456"]
