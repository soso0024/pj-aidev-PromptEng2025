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

def test_find_max_normal_cases():
    assert find_max(["hello", "world", "python"]) == "python"
    assert find_max(["abc", "def", "ghijk"]) == "ghijk"

def test_find_max_unique_chars():
    assert find_max(["aaa", "bbb", "abcde"]) == "abcde"
    assert find_max(["aaaa", "bbbb", "abcd"]) == "abcd"

def test_find_max_lexicographic_order():
    assert find_max(["cat", "act", "tac"]) == "cat"
    assert find_max(["abc", "acb", "bac"]) == "bac"

def test_find_max_single_element():
    assert find_max(["hello"]) == "hello"

def test_find_max_empty_list():
    with pytest.raises(IndexError):
        find_max([])

@pytest.mark.parametrize("words,expected", [
    (["apple", "banana", "cherry"], "cherry"),
    (["xyz", "abc", "pqr"], "xyz"),
    (["a", "aa", "aaa"], "aaa")
])
def test_find_max_parametrized(words, expected):
    assert find_max(words) == expected