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

@pytest.mark.parametrize("input_str,expected", [
    ("Hi, my name is John", ["Hi", "my", "name", "is", "John"]),
    ("One, two, three, four, five, six", ["One", "two", "three", "four", "five", "six"]),
    ("Hello World", ["Hello", "World"]),
    ("", []),
    ("Single", ["Single"]),
    ("Multiple    spaces", ["Multiple", "spaces"]),
    ("Comma,no,spaces", ["Comma", "no", "spaces"]),
    ("Mix,of spaces,and,commas", ["Mix", "of", "spaces", "and", "commas"]),
    ("   Leading spaces", ["Leading", "spaces"]),
    ("Trailing spaces   ", ["Trailing", "spaces"]),
    (",,Multiple,,commas,,", ["Multiple", "commas"]),
    ("Word,", ["Word"]),
    (",Word", ["Word"]),
    ("Hello,,,,World", ["Hello", "World"]),
    ("  Multiple  Spaces  Between  Words  ", ["Multiple", "Spaces", "Between", "Words"]),
])
def test_words_string_parametrized(input_str, expected):
    assert words_string(input_str) == expected

def test_words_string_none():
    assert words_string(None) == []

def test_words_string_non_string():
    with pytest.raises(TypeError):
        words_string(123)

def test_words_string_special_chars():
    assert words_string("Hello! @#$%^&* World") == ["Hello!", "@#$%^&*", "World"]

def test_words_string_numbers():
    assert words_string("1, 2, 3, 4, 5") == ["1", "2", "3", "4", "5"]

def test_words_string_mixed_content():
    assert words_string("Test123, abc-def, 99bottles") == ["Test123", "abc-def", "99bottles"]