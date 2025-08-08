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

def test_words_string_normal_cases():
    assert words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    assert words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]

def test_words_string_edge_cases():
    assert words_string("") == []
    assert words_string(" ") == []
    assert words_string(",") == []

@pytest.mark.parametrize("input_string,expected", [
    ("Hello, world", ["Hello", "world"]),
    ("Python,is,awesome", ["Python", "is", "awesome"]),
    ("Multiple   spaces,between words", ["Multiple", "spaces", "between", "words"]),
    ("Comma, separated, values", ["Comma", "separated", "values"]),
    ("Single", ["Single"])
])
def test_words_string_parametrized(input_string, expected):
    assert words_string(input_string) == expected

def test_words_string_mixed_delimiters():
    assert words_string("Hello, world, how are you") == ["Hello", "world", "how", "are", "you"]

def test_words_string_whitespace_handling():
    assert words_string("  Trim   whitespace  ") == ["Trim", "whitespace"]
