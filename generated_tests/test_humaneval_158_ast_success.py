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

def test_find_max_basic():
    assert find_max(["hello", "world"]) == "world"
    assert find_max(["a", "ab", "abc"]) == "abc"

def test_find_max_same_length():
    assert find_max(["cat", "dog", "rat"]) == "cat"
    assert find_max(["abc", "def", "ghi"]) == "abc"

def test_find_max_repeated_chars():
    assert find_max(["aaa", "bbb", "abcde"]) == "abcde"
    assert find_max(["hello", "world", "programming"]) == "programming"

@pytest.mark.parametrize("input_list,expected", [
    (["hello", "world", "python"], "python"),
    (["aaa", "bbb", "ccc"], "aaa"),
    (["abcde", "abcdef", "abc"], "abcdef"),
    (["test", "testing", "tested"], "testing"),
    (["a", "b", "c"], "a"),
    (["zzz", "aaa", "bbb"], "aaa"),
])
def test_find_max_parametrized(input_list, expected):
    assert find_max(input_list) == expected

def test_find_max_single_element():
    assert find_max(["test"]) == "test"

def test_find_max_empty_strings():
    assert find_max(["", "a", ""]) == "a"

def test_find_max_special_chars():
    assert find_max(["!@#", "abc", "123"]) == "!@#"

@pytest.mark.xfail(raises=IndexError)
def test_find_max_empty_list():
    find_max([])

def test_find_max_unicode():
    assert find_max(["über", "café", "résumé"]) == "résumé"

def test_find_max_mixed_case():
    assert find_max(["ABC", "abc", "AbC"]) == "ABC"

def test_find_max_whitespace():
    assert find_max(["  ", " a ", "b  "]) == " a "

def test_find_max_numbers_as_strings():
    assert find_max(["123", "456", "789"]) == "123"