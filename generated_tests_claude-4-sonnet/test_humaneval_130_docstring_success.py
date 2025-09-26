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
            my_tri.append(i / 2 + 1)
        else:
            my_tri.append(my_tri[i - 1] + my_tri[i - 2] + (i + 3) / 2)
    return my_tri

def test_tri_zero():
    assert tri(0) == [1]

def test_tri_one():
    assert tri(1) == [1, 3]

def test_tri_two():
    assert tri(2) == [1, 3, 2.0]

def test_tri_three():
    assert tri(3) == [1, 3, 2.0, 8.0]

def test_tri_four():
    result = tri(4)
    expected = [1, 3, 2.0, 8.0, 3.0]
    assert result == expected

def test_tri_five():
    result = tri(5)
    expected = [1, 3, 2.0, 8.0, 3.0, 15.0]
    assert result == expected

def test_tri_six():
    result = tri(6)
    expected = [1, 3, 2.0, 8.0, 3.0, 15.0, 4.0]
    assert result == expected

@pytest.mark.parametrize("n,expected_length", [
    (0, 1),
    (1, 2),
    (2, 3),
    (3, 4),
    (10, 11),
    (20, 21)
])
def test_tri_length(n, expected_length):
    result = tri(n)
    assert len(result) == expected_length

def test_tri_first_two_elements():
    for n in range(1, 10):
        result = tri(n)
        assert result[0] == 1
        assert result[1] == 3

def test_tri_even_positions():
    result = tri(10)
    assert result[2] == 2.0  # tri(2) = 1 + 2/2 = 2
    assert result[4] == 3.0  # tri(4) = 1 + 4/2 = 3
    assert result[6] == 4.0  # tri(6) = 1 + 6/2 = 4
    assert result[8] == 5.0  # tri(8) = 1 + 8/2 = 5
    assert result[10] == 6.0  # tri(10) = 1 + 10/2 = 6

def test_tri_large_number():
    result = tri(15)
    assert len(result) == 16
    assert result[0] == 1
    assert result[1] == 3

def test_tri_sequence_consistency():
    result = tri(7)
    assert result[3] == 8.0