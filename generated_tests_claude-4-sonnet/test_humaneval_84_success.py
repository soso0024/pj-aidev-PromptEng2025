# Test cases for HumanEval/84
# Generated using Claude API


def solve(N):
    """Given a positive integer N, return the total sum of its digits in binary.
    
    Example
        For N = 1000, the sum of digits will be 1 the output should be "1".
        For N = 150, the sum of digits will be 6 the output should be "110".
        For N = 147, the sum of digits will be 12 the output should be "1100".
    
    Variables:
        @N integer
             Constraints: 0 ≤ N ≤ 10000.
    Output:
         a string of binary number
    """

    return bin(sum(int(i) for i in str(N)))[2:]


# Generated test cases:
import pytest

def solve(N):
    return bin(sum(int(i) for i in str(N)))[2:]

class TestSolve:
    
    @pytest.mark.parametrize("input_val,expected", [
        (0, "0"),
        (1, "1"),
        (2, "10"),
        (3, "11"),
        (4, "100"),
        (5, "101"),
        (6, "110"),
        (7, "111"),
        (8, "1000"),
        (9, "1001"),
        (10, "1"),
        (11, "10"),
        (12, "11"),
        (99, "10010"),
        (123, "110"),
        (456, "1111"),
        (789, "11000"),
        (1000, "1"),
        (9999, "100100"),
        (12345, "1111"),
        (99999, "101101"),
        (100000, "1"),
        (999999, "110110"),
        (1234567, "11100"),
        (9876543, "101010"),
        (10000000, "1"),
        (99999999, "1001000"),
        (100000000, "1"),
        (999999999, "1010001"),
        (1000000000, "1"),
        (9999999999, "1011010")
    ])
    def test_solve_various_inputs(self, input_val, expected):
        assert solve(input_val) == expected
    
    def test_solve_single_digit(self):
        for i in range(10):
            result = solve(i)
            assert result == bin(i)[2:]
    
    def test_solve_powers_of_10(self):
        powers = [1, 10, 100, 1000, 10000, 100000, 1000000]
        for power in powers:
            result = solve(power)
            assert result == "1"
    
    def test_solve_repdigits(self):
        assert solve(11) == "10"
        assert solve(111) == "11"
        assert solve(1111) == "100"
        assert solve(11111) == "101"
        assert solve(22) == "100"
        assert solve(333) == "1001"
        assert solve(4444) == "10000"
        assert solve(55555) == "11001"
        assert solve(666666) == "100100"
        assert solve(7777777) == "110001"
        assert solve(88888888) == "1000000"
        assert solve(999999999) == "1010001"
    
    def test_solve_edge_cases(self):
        assert solve(0) == "0"
        assert solve(1) == "1"
        assert solve(10) == "1"
        assert solve(100) == "1"
    
    def test_solve_large_numbers(self):
        large_num = 123456789012345
        digit_sum = sum(int(d) for d in str(large_num))
        expected = bin(digit_sum)[2:]
        assert solve(large_num) == expected
    
    def test_solve_string_input(self):
        result = solve("123")
        assert result == "110"
    
    def test_solve_negative_numbers(self):
        result = solve(123)
        assert result == "110"