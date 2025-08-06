# Test cases for HumanEval/130
# Generated using Claude API


def tri(n):
    """Everyone knows Fibonacci sequence, it was studied deeply by mathematicians in 
    the last couple centuries. However, what people don't know is Tribonacci sequence.
    Tribonacci sequence is defined by the recurrence:
    tri(1) = 3
    tri(n) = 1 + n / 2, if n is even.
    tri(n) =  tri(n - 1) + tri(n - 2) + tri(n + 1), if n is odd.
    For example:
    tri(2) = 1 + (2 / 2) = 2
    tri(4) = 3
    tri(3) = tri(2) + tri(1) + tri(4)
           = 2 + 3 + 3 = 8 
    You are given a non-negative integer number n, you have to a return a list of the 
    first n + 1 numbers of the Tribonacci sequence.
    Examples:
    tri(3) = [1, 3, 2, 8]
    """

    if n == 0:
        return [1]
    my_tri = [1, 3]
    for i in range(2, n + 1):
        if i % 2 == 0:
            my_tri.append(i / 2 + 1)
        else:
            my_tri.append(my_tri[i - 1] + my_tri[i - 2] + (i + 3) / 2)
    return my_tri


# Generated test cases:
import pytest

def test_tri_zero():
    assert tri(0) == [1]

def test_tri_one():
    assert tri(1) == [1, 3]

def test_tri_two():
    assert tri(2) == [1, 3, 2]

def test_tri_three():
    assert tri(3) == [1, 3, 2, 8]

def test_tri_four():
    assert tri(4) == [1, 3, 2, 8, 3]

def test_tri_five():
    assert tri(5) == [1, 3, 2, 8, 3, 15]

@pytest.mark.parametrize("n,expected", [
    (0, [1]),
    (1, [1, 3]),
    (2, [1, 3, 2]),
    (3, [1, 3, 2, 8]),
    (4, [1, 3, 2, 8, 3]),
    (5, [1, 3, 2, 8, 3, 15])
])
def test_tri_parametrized(n, expected):
    assert tri(n) == expected

@pytest.mark.parametrize("invalid_input", [
    -1,
    -100,
    -1000
])
def test_tri_negative_input(invalid_input):
    try:
        result = tri(invalid_input)
        assert False, f"Expected ValueError for negative input {invalid_input}, but got result {result}"
    except IndexError:
        pass

@pytest.mark.parametrize("invalid_type", [
    "string",
    None,
    [],
    {},
    1.5
])
def test_tri_invalid_type(invalid_type):
    with pytest.raises((TypeError, AttributeError)):
        tri(invalid_type)

def test_tri_large_input():
    result = tri(10)
    assert len(result) == 11
    assert result[:6] == [1, 3, 2, 8, 3, 15]

def test_tri_sequence_properties():
    result = tri(6)
    assert result[0] == 1
    assert result[1] == 3
    assert all(isinstance(x, (int, float)) for x in result)