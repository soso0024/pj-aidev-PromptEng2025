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
        expression+= oprt + str(oprn)
    return eval(expression)

def test_basic_addition():
    assert do_algebra(['+'], [1, 2]) == 3

def test_basic_subtraction():
    assert do_algebra(['-'], [5, 3]) == 2

def test_basic_multiplication():
    assert do_algebra(['*'], [4, 3]) == 12

def test_basic_division():
    assert do_algebra(['/'], [10, 2]) == 5.0

def test_multiple_operations():
    assert do_algebra(['+', '*'], [2, 3, 4]) == 14

def test_multiple_operations_order():
    assert do_algebra(['*', '+'], [2, 3, 4]) == 10

def test_complex_expression():
    assert do_algebra(['+', '-', '*'], [1, 2, 3, 4]) == -9

def test_single_operand():
    assert do_algebra([], [42]) == 42

def test_negative_numbers():
    assert do_algebra(['+'], [-5, 3]) == -2

def test_float_numbers():
    assert do_algebra(['+'], [1.5, 2.5]) == 4.0

def test_power_operation():
    assert do_algebra(['**'], [2, 3]) == 8

def test_floor_division():
    assert do_algebra(['//'], [7, 2]) == 3

def test_modulo_operation():
    assert do_algebra(['%'], [10, 3]) == 1

def test_mixed_operations():
    assert do_algebra(['+', '/', '*'], [10, 5, 2, 3]) == 17.5

def test_zero_operand():
    assert do_algebra(['+'], [0, 5]) == 5

def test_zero_multiplication():
    assert do_algebra(['*'], [0, 100]) == 0

def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        do_algebra(['/'], [1, 0])

def test_empty_operators_single_operand():
    assert do_algebra([], [7]) == 7

def test_large_numbers():
    assert do_algebra(['+'], [1000000, 2000000]) == 3000000

def test_parentheses_not_supported():
    result = do_algebra(['+', '*'], [2, 3, 4])
    assert result == 14

def test_string_concatenation_like():
    assert do_algebra(['+'], [1, 1]) == 2

def test_multiple_same_operations():
    assert do_algebra(['+', '+', '+'], [1, 1, 1, 1]) == 4

def test_subtraction_chain():
    assert do_algebra(['-', '-'], [10, 3, 2]) == 5

def test_mixed_positive_negative():
    assert do_algebra(['-', '+'], [0, 5, 3]) == -2

def test_float_division():
    assert do_algebra(['/'], [1, 2]) == 0.5

def test_complex_calculation():
    assert do_algebra(['*', '+', '/'], [2, 3, 4, 2]) == 8.0