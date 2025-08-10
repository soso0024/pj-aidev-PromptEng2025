# Test cases for HumanEval/44
# Generated using Claude API



def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """

    ret = ""
    while x > 0:
        ret = str(x % base) + ret
        x //= base
    return ret


# Generated test cases:
import pytest

@pytest.mark.parametrize("x, base, expected", [
    (0, 2, "0"),
    (10, 2, "1010"),
    (42, 10, "42"),
    (100, 16, "64"),
    (-10, 2, ValueError),
    (10, 1, ValueError),
    (10, 0, ZeroDivisionError),
])
def test_change_base(x, base, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            change_base(x, base)
    else:
        assert change_base(x, base) == expected

def change_base(x: int, base: int):
    if x < 0 or base < 2:
        raise ValueError("x must be non-negative and base must be at least 2")
    if base == 0:
        raise ZeroDivisionError("base cannot be 0")

    ret = ""
    while x > 0:
        ret = str(x % base) + ret
        x //= base
    return ret