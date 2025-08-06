# Test cases for HumanEval/160
# Generated using Claude API


def do_algebra(operator, operand):
    """
    Given two lists operator, and operand. The first list has basic algebra operations, and 
    the second list is a list of integers. Use the two given lists to build the algebric 
    expression and return the evaluation of this expression.

    The basic algebra operations:
    Addition ( + ) 
    Subtraction ( - ) 
    Multiplication ( * ) 
    Floor division ( // ) 
    Exponentiation ( ** ) 

    Example:
    operator['+', '*', '-']
    array = [2, 3, 4, 5]
    result = 2 + 3 * 4 - 5
    => result = 9

    Note:
        The length of operator list is equal to the length of operand list minus one.
        Operand is a list of of non-negative integers.
        Operator list has at least one operator, and operand list has at least two operands.

    """

    expression = str(operand[0])
    for oprt, oprn in zip(operator, operand[1:]):
        expression+= oprt + str(oprn)
    return eval(expression)


# Generated test cases:
import pytest

def test_basic_addition():
    assert do_algebra(["+"], [1, 2]) == 3

def test_basic_subtraction():
    assert do_algebra(["-"], [10, 5]) == 5

def test_basic_multiplication():
    assert do_algebra(["*"], [4, 5]) == 20

def test_basic_division():
    assert do_algebra(["//"], [20, 4]) == 5

def test_multiple_operations():
    assert do_algebra(["+", "*", "-"], [2, 3, 4, 2]) == 12

@pytest.mark.parametrize("operators, operands, expected", [
    (["+", "+"], [1, 2, 3], 6),
    (["-", "-"], [10, 5, 3], 2),
    (["*", "*"], [2, 3, 4], 24),
    (["//", "//"], [24, 2, 3], 4),
    (["+", "*", "//", "-"], [2, 3, 4, 2, 1], 7)
])
def test_multiple_operations_parametrized(operators, operands, expected):
    assert do_algebra(operators, operands) == expected

def test_single_number():
    with pytest.raises((IndexError, ValueError)):
        do_algebra([], [5])

@pytest.mark.parametrize("operators, operands", [
    (["+"], [1]),  # Missing operand
    (["+", "+"], [1, 2]),  # Too few operands
    (["+"], [1, 2, 3]),  # Too many operands
    ([], []),  # Empty lists
])
def test_invalid_inputs(operators, operands):
    with pytest.raises((IndexError, ValueError)):
        do_algebra(operators, operands)

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        do_algebra(["//"], [10, 0])

def test_large_numbers():
    assert do_algebra(["+", "*"], [1000000, 2000000, 3]) == 7000000

def test_negative_numbers():
    assert do_algebra(["+", "-", "*"], [-1, 5, -3, 2]) == 10

def test_decimal_numbers():
    assert do_algebra(["+", "*"], [1.5, 2.5, 2]) == 6.5

def test_complex_expression():
    assert do_algebra(["+", "*", "//", "-", "+"], [1, 2, 3, 6, 2, 3]) == 3