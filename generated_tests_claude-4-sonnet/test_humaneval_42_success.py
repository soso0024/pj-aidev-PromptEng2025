# Test cases for HumanEval/42
# Generated using Claude API



def incr_list(l: list):
    """Return list with elements incremented by 1.
    >>> incr_list([1, 2, 3])
    [2, 3, 4]
    >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """

    return [(e + 1) for e in l]


# Generated test cases:
import pytest

def incr_list(l: list):
    return [(e + 1) for e in l]

def test_empty_list():
    assert incr_list([]) == []

def test_single_element():
    assert incr_list([5]) == [6]

def test_multiple_positive_integers():
    assert incr_list([1, 2, 3, 4, 5]) == [2, 3, 4, 5, 6]

def test_negative_integers():
    assert incr_list([-5, -2, -1]) == [-4, -1, 0]

def test_zero():
    assert incr_list([0]) == [1]

def test_mixed_positive_negative():
    assert incr_list([-3, 0, 2, -1, 5]) == [-2, 1, 3, 0, 6]

def test_large_numbers():
    assert incr_list([999999, 1000000]) == [1000000, 1000001]

def test_floats():
    result = incr_list([1.5, 2.7, -0.3])
    expected = [2.5, 3.7, 0.7]
    assert len(result) == len(expected)
    for i in range(len(result)):
        assert abs(result[i] - expected[i]) < 1e-10

def test_mixed_int_float():
    result = incr_list([1, 2.5, 3])
    expected = [2, 3.5, 4]
    assert result == expected

@pytest.mark.parametrize("input_list,expected", [
    ([1], [2]),
    ([0, 0, 0], [1, 1, 1]),
    ([-10, 10], [-9, 11]),
    ([100, 200, 300], [101, 201, 301])
])
def test_parametrized_cases(input_list, expected):
    assert incr_list(input_list) == expected

def test_string_elements_raises_error():
    with pytest.raises(TypeError):
        incr_list(['a', 'b', 'c'])

def test_mixed_string_int_raises_error():
    with pytest.raises(TypeError):
        incr_list([1, 'hello', 3])

def test_none_elements_raises_error():
    with pytest.raises(TypeError):
        incr_list([1, None, 3])

def test_list_with_list_elements_raises_error():
    with pytest.raises(TypeError):
        incr_list([1, [2, 3], 4])

def test_boolean_elements():
    assert incr_list([True, False]) == [2, 1]

def test_very_long_list():
    input_list = list(range(1000))
    expected = list(range(1, 1001))
    assert incr_list(input_list) == expected
