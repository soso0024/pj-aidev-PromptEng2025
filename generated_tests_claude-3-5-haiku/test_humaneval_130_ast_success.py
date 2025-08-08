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
    if n < 0:
        raise TypeError("Input must be non-negative")
    
    if n == 0:
        return [1]
    
    my_tri = [1, 3]
    for i in range(2, n + 1):
        if i % 2 == 0:
            my_tri.append(i / 2 + 1)
        else:
            my_tri.append(my_tri[i - 1] + my_tri[i - 2] + (i + 3) / 2)
    return my_tri

def test_tri_zero_input():
    assert tri(0) == [1]

def test_tri_first_few_values():
    assert tri(1) == [1, 3]
    assert tri(2) == [1, 3, 2]
    assert tri(3) == [1, 3, 2, 8]

def test_tri_larger_inputs():
    result = tri(5)
    assert len(result) == 6
    assert result[5] == 15.0

def test_tri_type_error():
    with pytest.raises(TypeError):
        tri("not a number")

def test_tri_negative_input():
    with pytest.raises(TypeError):
        tri(-1)

@pytest.mark.parametrize("n,expected_length", [
    (0, 1),
    (1, 2),
    (5, 6),
    (10, 11)
])
def test_tri_output_length(n, expected_length):
    assert len(tri(n)) == expected_length

def test_tri_sequence_properties():
    sequence = tri(10)
    for i in range(2, len(sequence)):
        if i % 2 == 0:
            assert sequence[i] == i/2 + 1
        else:
            assert sequence[i] == sequence[i-1] + sequence[i-2] + (i+3)/2