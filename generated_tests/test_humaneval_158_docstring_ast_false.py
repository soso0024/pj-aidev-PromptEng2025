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

def test_basic_functionality():
    assert find_max(["name", "of", "string"]) == "string"
    assert find_max(["name", "enam", "game"]) == "enam"
    assert find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"

@pytest.mark.parametrize("input_list,expected", [
    (["hello", "world", "python"], "python"),
    (["cat", "dog", "elephant"], "elephant"),
    (["aaa", "bbb", "ccc"], "aaa"),
    (["test", "tset", "ttse"], "test"),
    (["", "a", "aa"], "aa"),
    (["xyz", "abc", "def"], "abc"),
    (["programming", "code", "developer"], "developer"),
    (["!!!!", "@@@@", "####"], "!!!!"),
    (["aabbcc", "abcdef", "abcd"], "abcdef"),
    (["same", "emas", "mase"], "emas")
])
def test_parametrized_cases(input_list, expected):
    assert find_max(input_list) == expected

def test_single_element():
    assert find_max(["test"]) == "test"

def test_empty_strings():
    assert find_max(["", "", ""]) == ""

def test_special_characters():
    assert find_max(["!@#", "$%^", "&*()"]) == "!@#"

def test_numbers_as_strings():
    assert find_max(["123", "456", "789"]) == "123"

def test_mixed_case():
    assert find_max(["ABC", "abc", "AbC"]) == "ABC"

def test_spaces():
    assert find_max(["a b", "a  b", "a   b"]) == "a b"

@pytest.mark.parametrize("input_list", [
    None,
    [None],
    [1, 2, 3],
    ["test", None, "abc"]
])
def test_invalid_inputs(input_list):
    with pytest.raises((ValueError, TypeError, AttributeError)):
        find_max(input_list)

def test_empty_list():
    with pytest.raises(IndexError):
        find_max([])

def test_unicode_strings():
    assert find_max(["über", "café", "résumé"]) == "café"

def test_same_unique_chars_different_lengths():
    assert find_max(["aaa", "a", "aaaaa"]) == "a"

def test_all_same_chars():
    assert find_max(["aaa", "aaa", "aaa"]) == "aaa"