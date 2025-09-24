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

def test_find_max_basic_cases():
    assert find_max(["name", "of", "string"]) == "string"
    assert find_max(["name", "enam", "game"]) == "enam"
    assert find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"

def test_find_max_single_word():
    assert find_max(["hello"]) == "hello"
    assert find_max(["a"]) == "a"
    assert find_max([""]) == ""

def test_find_max_empty_strings():
    assert find_max(["", "", ""]) == ""
    assert find_max(["abc", "", "def"]) == "abc"

def test_find_max_same_unique_count():
    assert find_max(["abc", "def"]) == "abc"
    assert find_max(["xyz", "abc"]) == "abc"
    assert find_max(["cat", "dog", "bat"]) == "bat"

def test_find_max_lexicographical_order():
    assert find_max(["ba", "ab"]) == "ab"
    assert find_max(["zzz", "aaa"]) == "aaa"
    assert find_max(["hello", "world"]) == "world"

def test_find_max_repeated_characters():
    assert find_max(["aaa", "bbb", "ccc"]) == "aaa"
    assert find_max(["aaab", "bbbc", "cccd"]) == "aaab"

def test_find_max_mixed_lengths():
    assert find_max(["a", "ab", "abc", "abcd"]) == "abcd"
    assert find_max(["abcd", "abc", "ab", "a"]) == "abcd"

def test_find_max_duplicate_words():
    assert find_max(["hello", "hello", "world"]) == "world"
    assert find_max(["abc", "abc", "def"]) == "abc"

@pytest.mark.parametrize("words,expected", [
    (["python", "java", "c"], "python"),
    (["test", "set", "net"], "net"),
    (["unique", "chars", "count"], "chars"),
    (["aa", "bb", "cc"], "aa"),
    (["programming", "code", "debug"], "programming")
])
def test_find_max_parametrized(words, expected):
    assert find_max(words) == expected

def test_find_max_special_characters():
    assert find_max(["a!b", "c@d", "e#f"]) == "a!b"
    assert find_max(["123", "456", "789"]) == "123"

def test_find_max_case_sensitivity():
    assert find_max(["Aa", "BB", "cc"]) == "Aa"
    assert find_max(["Hello", "WORLD", "test"]) == "WORLD"