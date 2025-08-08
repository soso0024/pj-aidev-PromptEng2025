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
    if not words:
        return ""
    return sorted(words, key = lambda x: (-len(set(x)), x))[0]

def test_find_max_normal_cases():
    assert find_max(["name", "of", "string"]) == "string"
    assert find_max(["name", "enam", "game"]) == "enam"
    assert find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"

def test_find_max_lexicographical_order():
    assert find_max(["abc", "abd", "abe"]) == "abc"
    assert find_max(["hello", "world", "python"]) == "python"

def test_find_max_edge_cases():
    assert find_max([]) == ""
    assert find_max(["a", "b", "c"]) == "a"
    assert find_max(["", "x", "yz"]) == "yz"

@pytest.mark.parametrize("words,expected", [
    (["name", "of", "string"], "string"),
    (["name", "enam", "game"], "enam"),
    (["aaaaaaa", "bb", "cc"], "aaaaaaa"),
    (["abc", "abd", "abe"], "abc"),
    (["hello", "world", "python"], "python"),
    ([], ""),
    (["a", "b", "c"], "a"),
    (["", "x", "yz"], "yz")
])
def test_find_max_parametrized(words, expected):
    assert find_max(words) == expected