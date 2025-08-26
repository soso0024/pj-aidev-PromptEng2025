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

def tri(n):
    if n == 0:
        return [1]
    my_tri = [1, 3]
    for i in range(2, n + 1):
        if i % 2 == 0:
            my_tri.append(1 + i / 2)
        else:
            my_tri.append(my_tri[i - 1] + my_tri[i - 2] + (i + 1) / 2)
    return my_tri

def test_tri_zero_input():
    assert tri(0) == [1]

def test_tri_small_inputs():
    assert tri(1) == [1, 3]
    assert tri(2) == [1, 3, 2]
    assert tri(3) == [1, 3, 2, 8]

def test_tri_larger_inputs():
    result = tri(5)
    assert len(result) == 6
    assert result[0] == 1
    assert result[1] == 3

@pytest.mark.parametrize("n,expected_length", [
    (0, 1),
    (1, 2),
    (2, 3),
    (3, 4),
    (5, 6),
    (10, 11)
])
def test_tri_sequence_length(n, expected_length):
    assert len(tri(n)) == expected_length

def test_tri_sequence_properties():
    sequence = tri(6)
    assert sequence[2] == 2
    assert sequence[3] == 8

def test_tri_type_consistency():
    result = tri(4)
    assert all(isinstance(x, (int, float)) for x in result)

def test_tri_increasing_sequence():
    sequence = tri(7)
    for i in range(1, len(sequence)):
        assert sequence[i] >= sequence[i-1] or abs(sequence[i] - sequence[i-1]) < 1e-10