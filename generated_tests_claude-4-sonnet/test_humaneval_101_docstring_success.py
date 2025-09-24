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
    assert words_string("Hello") == ["Hello"]

def test_words_with_spaces():
    assert words_string("Hi my name is John") == ["Hi", "my", "name", "is", "John"]

def test_words_with_commas():
    assert words_string("One,two,three,four,five,six") == ["One", "two", "three", "four", "five", "six"]

def test_words_with_commas_and_spaces():
    assert words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]

def test_words_with_multiple_spaces():
    assert words_string("Hi  my   name    is John") == ["Hi", "my", "name", "is", "John"]

def test_words_with_multiple_commas():
    assert words_string("One,,two,,,three") == ["One", "two", "three"]

def test_words_with_commas_spaces_mixed():
    assert words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]

def test_leading_trailing_spaces():
    assert words_string("  Hello world  ") == ["Hello", "world"]

def test_leading_trailing_commas():
    assert words_string(",Hello,world,") == ["Hello", "world"]

def test_only_spaces():
    assert words_string("   ") == []

def test_only_commas():
    assert words_string(",,,") == []

def test_only_commas_and_spaces():
    assert words_string(", , ,") == []

def test_single_character_words():
    assert words_string("a,b,c") == ["a", "b", "c"]

def test_mixed_punctuation_in_words():
    assert words_string("Hello!, How are you?") == ["Hello!", "How", "are", "you?"]

def test_numbers_as_words():
    assert words_string("1, 2, 3, 4") == ["1", "2", "3", "4"]

def test_special_characters():
    assert words_string("@#$, %^&") == ["@#$", "%^&"]

@pytest.mark.parametrize("input_str,expected", [
    ("", []),
    ("word", ["word"]),
    ("a,b", ["a", "b"]),
    ("a b", ["a", "b"]),
    ("a, b", ["a", "b"]),
    ("  a  ,  b  ", ["a", "b"]),
    ("one,two,three", ["one", "two", "three"]),
    ("one two three", ["one", "two", "three"]),
    ("one, two, three", ["one", "two", "three"])
])
def test_parametrized_cases(input_str, expected):
    assert words_string(input_str) == expected
