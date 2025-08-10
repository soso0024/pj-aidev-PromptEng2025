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

def do_algebra(operator, operand):
    expression = str(operand[0])
    for oprt, oprn in zip(operator, operand[1:]):
        expression += oprt + str(oprn)
    return eval(expression)

def test_do_algebra_addition():
    assert do_algebra(['+'], [2, 3]) == 5
    assert do_algebra(['+'], [0, 0]) == 0
    assert do_algebra(['+'], [-2, 5]) == 3

def test_do_algebra_subtraction():
    assert do_algebra(['-'], [10, 4]) == 6
    assert do_algebra(['-'], [0, 0]) == 0
    assert do_algebra(['-'], [5, 2]) == 3

def test_do_algebra_multiplication():
    assert do_algebra(['*'], [2, 3]) == 6
    assert do_algebra(['*'], [0, 5]) == 0
    assert do_algebra(['*'], [-2, 3]) == -6

def test_do_algebra_division():
    assert do_algebra(['//', 10, 5]) == 2
    assert do_algebra(['//', 0, 5]) == 0
    with pytest.raises(ZeroDivisionError):
        do_algebra(['//', 10, 0])

@pytest.mark.parametrize("operator,operand,expected", [
    (['+'], [2.5, 3.7], 6.2),
    (['-'], [7.8, 2.1], 5.7),
    ['*', [2.5, 3.0], 7.5],
    ['//', [10.0, 2.5], 4.0]
])
def test_do_algebra_float(operator, operand, expected):
    assert do_algebra(operator, operand) == expected

def test_do_algebra_invalid_operator():
    with pytest.raises(TypeError):
        do_algebra(['%'], [10, 3])

def test_do_algebra_empty_input():
    with pytest.raises(IndexError):
        do_algebra([], [])
    with pytest.raises(IndexError):
        do_algebra(['+'], [])