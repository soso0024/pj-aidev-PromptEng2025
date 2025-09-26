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

def words_string(s):
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

def test_empty_string():
    assert words_string("") == []

def test_none_input():
    assert words_string(None) == []

def test_single_word():
    assert words_string("hello") == ["hello"]

def test_multiple_words_with_commas():
    assert words_string("hello,world") == ["hello", "world"]

def test_multiple_words_with_spaces():
    assert words_string("hello world") == ["hello", "world"]

def test_mixed_commas_and_spaces():
    assert words_string("hello, world") == ["hello", "world"]

def test_multiple_consecutive_commas():
    assert words_string("hello,,world") == ["hello", "world"]

def test_multiple_consecutive_spaces():
    assert words_string("hello  world") == ["hello", "world"]

def test_leading_comma():
    assert words_string(",hello") == ["hello"]

def test_trailing_comma():
    assert words_string("hello,") == ["hello"]

def test_leading_space():
    assert words_string(" hello") == ["hello"]

def test_trailing_space():
    assert words_string("hello ") == ["hello"]

def test_only_commas():
    assert words_string(",,,") == []

def test_only_spaces():
    assert words_string("   ") == []

def test_mixed_only_commas_and_spaces():
    assert words_string(", , ,") == []

def test_complex_string():
    assert words_string("one,two three,four") == ["one", "two", "three", "four"]

def test_single_character():
    assert words_string("a") == ["a"]

def test_single_comma():
    assert words_string(",") == []

def test_single_space():
    assert words_string(" ") == []

@pytest.mark.parametrize("input_str,expected", [
    ("hello,world,test", ["hello", "world", "test"]),
    ("a,b,c,d", ["a", "b", "c", "d"]),
    ("word1 word2 word3", ["word1", "word2", "word3"]),
    ("mix,ed spa ces,here", ["mix", "ed", "spa", "ces", "here"]),
    ("", []),
    ("single", ["single"])
])
def test_parametrized_cases(input_str, expected):
    assert words_string(input_str) == expected
