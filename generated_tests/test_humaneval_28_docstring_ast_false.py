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
    (["a", "", "b"], "ab"),
    ([" "], " "),
    (["特", "殊", "字"], "特殊字"),
    (["a\n", "b\t", "c"], "a\nb\tc"),
])
def test_concatenate_valid_inputs(input_list, expected, concatenate):
    assert concatenate(input_list) == expected


def test_concatenate_empty_list(concatenate):
    assert concatenate([]) == ""


def test_concatenate_single_element(concatenate):
    assert concatenate(["test"]) == "test"


def test_concatenate_with_numbers(concatenate):
    with pytest.raises(TypeError):
        concatenate([1, 2, 3])


def test_concatenate_with_none(concatenate):
    with pytest.raises(TypeError):
        concatenate([None])


def test_concatenate_with_mixed_types(concatenate):
    with pytest.raises(TypeError):
        concatenate(["a", 1, "b"])


def test_concatenate_invalid_input_type(concatenate):
    with pytest.raises(TypeError):
        concatenate("not a list")


def test_concatenate_nested_lists(concatenate):
    with pytest.raises(TypeError):
        concatenate(["a", ["b"], "c"])


def test_concatenate_large_input(concatenate):
    large_list = ["a"] * 1000000
    assert concatenate(large_list) == "a" * 1000000


@pytest.fixture
def concatenate():
    def _concatenate(strings: List[str]) -> str:
        return ''.join(strings)
    return _concatenate