# Test cases for HumanEval/155
# Generated using Claude API


def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """

    even_count = 0
    odd_count = 0
    for i in str(abs(num)):
        if int(i)%2==0:
            even_count +=1
        else:
            odd_count +=1
    return (even_count, odd_count)


# Generated test cases:
from pytest import raises, mark

@mark.parametrize("num,expected", [
    (0, (1, 0)),
    (1, (0, 1)),
    (-1, (0, 1)),
    (12345, (2, 3)),
    (-12345, (2, 3)),
    (1000000, (6, 0)),
    (-1000000, (6, 0)),
    (float('inf'), TypeError),
    (float('-inf'), TypeError),
    ('abc', TypeError),
    (None, TypeError)
])
def test_even_odd_count(num, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with raises(expected):
            even_odd_count(num)
    else:
        assert even_odd_count(num) == expected

def even_odd_count(num):
    even_count = 0
    odd_count = 0
    for i in str(abs(int(num))):
        if int(i) % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return (even_count, odd_count)