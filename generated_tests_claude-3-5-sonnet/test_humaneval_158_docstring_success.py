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

@pytest.mark.parametrize("words,expected", [
    (["name", "of", "string"], "string"),
    (["name", "enam", "game"], "enam"),
    (["aaaaaaa", "bb", "cc"], "aaaaaaa"),
    (["hello", "world", "python"], "python"),
    (["a", "ab", "abc"], "abc"),
    (["zzz", "aaa", "bbb"], "aaa"),
    (["test", "tset", "ttse"], "test"),
    (["", "a", "b"], "a"),
    (["xyz", "xyz", "xyz"], "xyz"),
    (["abcdef", "fedcba", "abcdef"], "abcdef"),
    (["!@#", "123", "abc"], "!@#"),
    (["aaa", "bbb", "ccc"], "aaa"),
    (["short", "longer", "longest"], "longest"),
    (["unique", "repeated", "uniiique"], "repeated"),
])
def test_find_max_normal_cases(words, expected):
    assert find_max(words) == expected

def test_find_max_single_element():
    assert find_max(["test"]) == "test"

def test_find_max_empty_strings():
    assert find_max(["", "", ""]) == ""

@pytest.mark.parametrize("invalid_input", [
    None,
    [1, 2, 3],
    ["test", None, "abc"],
    ["test", 123, "abc"],
])
def test_find_max_invalid_input(invalid_input):
    with pytest.raises((ValueError, TypeError, AttributeError)):
        find_max(invalid_input)

def test_find_max_empty_list():
    with pytest.raises(IndexError):
        find_max([])

def test_find_max_special_characters():
    assert find_max(["@#$", "!@#", "123"]) == "!@#"

def test_find_max_whitespace():
    assert find_max(["  ", " ", "   "]) == " "

def test_find_max_case_sensitivity():
    assert find_max(["ABC", "abc", "AbC"]) == "ABC"

def test_find_max_unicode():
    assert find_max(["über", "café", "naïve"]) == "naïve"