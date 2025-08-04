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
    ("", []),
    ("hello", ["hello"]),
    ("hello,world", ["hello", "world"]),
    ("one,two,three", ["one", "two", "three"]),
    ("multiple   spaces", ["multiple", "spaces"]),
    ("trailing,   spaces  ", ["trailing", "spaces"]),
    ("mixed,separators spaces", ["mixed", "separators", "spaces"]),
    ("single,", ["single"]),
    (",leading", ["leading"]),
    (",,multiple,,commas,,", ["multiple", "commas"]),
    ("special!@#$chars", ["special!@#$chars"]),
    ("numbers123,456", ["numbers123", "456"]),
    ("  whitespace  ", ["whitespace"]),
    ("one,two,,three", ["one", "two", "three"]),
    ("complex,   mixed   ,case,  test", ["complex", "mixed", "case", "test"])
])
def test_words_string_parametrized(input_str, expected):
    assert words_string(input_str) == expected

def test_words_string_none():
    assert words_string(None) == []

def test_words_string_special_chars():
    assert words_string("hello world,test") == ["hello", "world", "test"]
    assert words_string("tab here,now") == ["tab", "here", "now"]

def test_words_string_unicode():
    assert words_string("über,café") == ["über", "café"]
    assert words_string("你好,世界") == ["你好", "世界"]