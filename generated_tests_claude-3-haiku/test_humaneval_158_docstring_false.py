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
    assert find_max(["name", "of", "string"]) == "string"
    assert find_max(["name", "enam", "game"]) == "enam"
    assert find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"

def test_find_max_empty_list():
    assert find_max([]) == ""

def test_find_max_single_element():
    assert find_max(["hello"]) == "hello"

def test_find_max_all_equal():
    assert find_max(["aaa", "aaa", "aaa"]) == "aaa"

def test_find_max_all_unique():
    assert find_max(["abc", "def", "ghi"]) == "abc"

@pytest.mark.parametrize("words,expected", [
    (["apple", "banana", "cherry"], "cherry"),
    (["dog", "cat", "bird"], "bird"),
    (["red", "green", "blue"], "blue"),
    (["hello", "world", "python"], "python"),
])
def test_find_max_parametrized(words, expected):
    assert find_max(words) == expected