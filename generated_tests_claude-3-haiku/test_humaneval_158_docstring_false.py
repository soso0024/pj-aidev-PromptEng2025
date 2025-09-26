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
from solution import find_max
import pytest

@pytest.mark.parametrize("words,expected", [
    (["name", "of", "string"], "string"),
    (["name", "enam", "game"], "enam"),
    (["aaaaaaa", "bb", "cc"], "aaaaaaa"),
    ([], ""),
    (["a"], "a"),
    (["aa", "bb"], "aa"),
    (["abc", "def", "ghi"], "abc"),
    (["aaa", "bbb", "ccc"], "aaa"),
    (["hello", "world", "python"], "python"),
    (["unique", "characters", "maximum"], "characters")
])
def test_find_max(words, expected):
    assert find_max(words) == expected

def test_find_max_empty_list():
    assert find_max([]) == ""

def test_find_max_single_element_list():
    assert find_max(["a"]) == "a"

def test_find_max_multiple_equal_length_strings():
    assert find_max(["aa", "bb"]) == "aa"

def test_find_max_multiple_equal_unique_characters():
    assert find_max(["abc", "def", "ghi"]) == "abc"

def test_find_max_multiple_equal_unique_characters_different_order():
    assert find_max(["cba", "fed", "ihg"]) == "cba"