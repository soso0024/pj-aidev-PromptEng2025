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
    assert do_algebra(['+'], [2, 3]) == 5

def test_basic_subtraction():
    assert do_algebra(['-'], [5, 3]) == 2

def test_basic_multiplication():
    assert do_algebra(['*'], [4, 5]) == 20

def test_basic_floor_division():
    assert do_algebra(['//'], [10, 3]) == 3

def test_basic_exponentiation():
    assert do_algebra(['**'], [2, 3]) == 8

@pytest.mark.parametrize("operators,operands,expected", [
    (['+', '*', '-'], [2, 3, 4, 5], 9),
    (['*', '+', '//'], [2, 3, 4, 2], 8),
    (['+', '**', '*'], [1, 2, 3, 2], 17),
    (['-', '-', '-'], [10, 2, 3, 1], 4),
    (['*', '*', '*'], [2, 2, 2, 2], 16)
])
def test_multiple_operations(operators, operands, expected):
    assert do_algebra(operators, operands) == expected

def test_single_operation_large_numbers():
    assert do_algebra(['*'], [1000, 1000]) == 1000000

def test_exponentiation_zero():
    assert do_algebra(['**'], [5, 0]) == 1

def test_floor_division_exact():
    assert do_algebra(['//'], [10, 2]) == 5

@pytest.mark.parametrize("operators,operands,expected", [
    (['**', '**'], [2, 2, 2], 16),
    (['*', '//'], [10, 2, 2], 10),
    (['+', '-'], [5, 3, 2], 6)
])
def test_operator_precedence(operators, operands, expected):
    assert do_algebra(operators, operands) == expected

@pytest.mark.xfail(raises=ZeroDivisionError)
def test_division_by_zero():
    do_algebra(['//'], [5, 0])

@pytest.mark.xfail(raises=ValueError)
def test_invalid_operator():
    do_algebra(['%'], [5, 2])

def test_large_expression():
    operators = ['+', '*', '-', '//', '**']
    operands = [1, 2, 3, 4, 2, 3]
    assert do_algebra(operators, operands) == 7

def test_all_additions():
    operators = ['+'] * 4
    operands = [1, 2, 3, 4, 5]
    assert do_algebra(operators, operands) == 15

def test_all_multiplications():
    operators = ['*'] * 3
    operands = [2, 2, 2, 2]
    assert do_algebra(operators, operands) == 16

def test_alternating_operations():
    operators = ['+', '-', '+', '-']
    operands = [10, 5, 3, 2, 1]
    assert do_algebra(operators, operands) == 13