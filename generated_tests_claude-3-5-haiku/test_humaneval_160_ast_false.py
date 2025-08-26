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

def test_do_algebra_basic_addition():
    assert do_algebra(['+'], [1, 2]) == 3

def test_do_algebra_multiple_operations():
    assert do_algebra(['+', '*'], [1, 2, 3]) == 7

def test_do_algebra_subtraction():
    assert do_algebra(['-'], [10, 5]) == 5

def test_do_algebra_division():
    assert do_algebra(['/'], [10, 2]) == 5.0

def test_do_algebra_complex_expression():
    assert do_algebra(['+', '*', '-'], [1, 2, 3, 4]) == -5

@pytest.mark.parametrize("operators,operands,expected", [
    (['+'], [5, 3], 8),
    (['-'], [10, 4], 6),
    (['*'], [2, 6], 12),
    (['/'], [15, 3], 5.0),
    (['+', '*'], [2, 3, 4], 14),
    (['-', '+'], [10, 5, 3], 8)
])
def test_do_algebra_parametrized(operators, operands, expected):
    assert do_algebra(operators, operands) == expected

def test_do_algebra_single_number():
    assert do_algebra([], [42]) == 42

def test_do_algebra_zero_division():
    with pytest.raises(ZeroDivisionError):
        do_algebra(['/'], [10, 0])

def test_do_algebra_invalid_operator():
    with pytest.raises(SyntaxError):
        do_algebra(['%'], [10, 3])