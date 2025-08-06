# Test cases for HumanEval/106
# Generated using Claude API


def f(n):
    """ Implement the function f that takes n as a parameter,
    and returns a list of size n, such that the value of the element at index i is the factorial of i if i is even
    or the sum of numbers from 1 to i otherwise.
    i starts from 1.
    the factorial of i is the multiplication of the numbers from 1 to i (1 * 2 * ... * i).
    Example:
    f(5) == [1, 2, 6, 24, 15]
    """

    ret = []
    for i in range(1,n+1):
        if i%2 == 0:
            x = 1
            for j in range(1,i+1): x *= j
            ret += [x]
        else:
            x = 0
            for j in range(1,i+1): x += j
            ret += [x]
    return ret


# Generated test cases:
import pytest

def test_basic_case():
    assert f(5) == [1, 2, 6, 24, 15]

def test_single_element():
    assert f(1) == [1]

def test_two_elements():
    assert f(2) == [1, 2]

def test_three_elements():
    assert f(3) == [1, 2, 6]

@pytest.mark.parametrize("n,expected", [
    (4, [1, 2, 6, 24]),
    (6, [1, 2, 6, 24, 15, 720]),
    (7, [1, 2, 6, 24, 15, 720, 28]),
])
def test_various_lengths(n, expected):
    assert f(n) == expected

def test_empty_list():
    assert f(0) == []

@pytest.mark.parametrize("invalid_input", [
    -1,
    -100,
])
def test_negative_input(invalid_input):
    assert f(invalid_input) == []

@pytest.mark.parametrize("n,expected_length", [
    (10, 10),
    (20, 20),
    (1, 1),
])
def test_output_length(n, expected_length):
    assert len(f(n)) == expected_length

def test_large_number():
    result = f(10)
    assert result[9] == 3628800  # factorial of 10 (since 10 is even)
    assert result[8] == 45  # sum of 1 to 9

@pytest.mark.parametrize("invalid_type", [
    "string",
    None,
    3.14,
    [],
    {},
])
def test_invalid_types(invalid_type):
    with pytest.raises((TypeError, ValueError)):
        f(invalid_type)

def test_first_element_always_one():
    for i in range(1, 10):
        assert f(i)[0] == 1

def test_alternating_pattern():
    result = f(6)
    # Odd indices should be sums
    assert result[0] == 1  # sum of 1
    assert result[2] == 6  # sum of 1+2+3
    assert result[4] == 15  # sum of 1+2+3+4+5
    # Even indices should be factorials
    assert result[1] == 2  # factorial of 2
    assert result[3] == 24  # factorial of 4
    assert result[5] == 720  # factorial of 6