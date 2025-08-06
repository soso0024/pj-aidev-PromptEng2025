# Test cases for HumanEval/28
# Generated using Claude API

from typing import List


def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """

    return ''.join(strings)


# Generated test cases:
import pytest
from typing import List


@pytest.mark.parametrize("input_list,expected", [
    ([], ""),
    (["a"], "a"),
    (["a", "b", "c"], "abc"),
    (["hello", " ", "world"], "hello world"),
    (["", "", ""], ""),
    (["1", "2", "3"], "123"),
    ([" "], " "),
    (["特", "殊", "字"], "特殊字"),
    (["a", "", "b"], "ab"),
    (["", "test", ""], "test")
])
def test_concatenate_valid_inputs(input_list, expected):
    assert concatenate(input_list) == expected


def test_concatenate_empty_list():
    assert concatenate([]) == ""


def test_concatenate_single_empty_string():
    assert concatenate([""]) == ""


def test_concatenate_multiple_empty_strings():
    assert concatenate(["", "", ""]) == ""


def test_concatenate_with_spaces():
    assert concatenate([" ", " ", " "]) == "   "


@pytest.mark.parametrize("invalid_input", [
    None,
    123,
    ["a", 1, "b"],
    ["a", None, "b"],
    [True, False],
    [3.14, "pi"]
])
def test_concatenate_invalid_inputs(invalid_input):
    with pytest.raises((TypeError, AttributeError)):
        concatenate(invalid_input)
