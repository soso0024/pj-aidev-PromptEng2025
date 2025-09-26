# Test cases for HumanEval/158
# Generated using Claude API


def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """

    return sorted(words, key = lambda x: (-len(set(x)), x))[0]


# Generated test cases:
import pytest

def find_max(words):
    return sorted(words, key = lambda x: (-len(set(x)), x))[0]

def test_find_max_single_word():
    assert find_max(["hello"]) == "hello"

def test_find_max_different_unique_char_counts():
    assert find_max(["abc", "ab", "a"]) == "abc"

def test_find_max_same_unique_char_counts_lexicographic():
    assert find_max(["abc", "def"]) == "abc"

def test_find_max_repeated_characters():
    assert find_max(["aaa", "abc"]) == "abc"

def test_find_max_mixed_lengths_and_unique_chars():
    assert find_max(["hello", "world", "hi", "python"]) == "python"

def test_find_max_empty_strings():
    assert find_max([""]) == ""

def test_find_max_with_empty_and_non_empty():
    assert find_max(["", "a"]) == "a"

def test_find_max_identical_words():
    assert find_max(["test", "test", "test"]) == "test"

def test_find_max_case_sensitive():
    assert find_max(["ABC", "abc"]) == "ABC"

def test_find_max_special_characters():
    assert find_max(["!@#", "abc", "123"]) == "!@#"

def test_find_max_numbers_as_strings():
    assert find_max(["123", "12", "1234"]) == "1234"

def test_find_max_tie_breaker_lexicographic():
    assert find_max(["ba", "ab"]) == "ab"

def test_find_max_long_words_with_repeated_chars():
    assert find_max(["aaaaaaa", "abcdefg"]) == "abcdefg"

def test_find_max_unicode_characters():
    assert find_max(["αβγ", "abc"]) == "abc"

def test_find_max_whitespace():
    assert find_max([" ", "a"]) == " "

def test_find_max_multiple_empty_strings():
    assert find_max(["", "", ""]) == ""

@pytest.mark.parametrize("words,expected", [
    (["a", "bb", "ccc"], "a"),
    (["xyz", "abc", "def"], "abc"),
    (["hello", "world"], "world"),
    (["python", "java", "c"], "python")
])
def test_find_max_parametrized(words, expected):
    assert find_max(words) == expected

def test_find_max_raises_index_error_empty_list():
    with pytest.raises(IndexError):
        find_max([])