# Test cases for HumanEval/75
# Generated using Claude API


def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """

    def is_prime(n):
        for j in range(2,n):
            if n%j == 0:
                return False
        return True

    for i in range(2,101):
        if not is_prime(i): continue
        for j in range(2,101):
            if not is_prime(j): continue
            for k in range(2,101):
                if not is_prime(k): continue
                if i*j*k == a: return True
    return False


# Generated test cases:
import pytest

def is_multiply_prime(a):
    def is_prime(n):
        for j in range(2,n):
            if n%j == 0:
                return False
        return True

    for i in range(2,101):
        if not is_prime(i): continue
        for j in range(2,101):
            if not is_prime(j): continue
            for k in range(2,101):
                if not is_prime(k): continue
                if i*j*k == a: return True
    return False

def test_is_multiply_prime_basic_cases():
    assert is_multiply_prime(30) == True  # 2*3*5
    assert is_multiply_prime(8) == True   # 2*2*2
    assert is_multiply_prime(10) == False
    assert is_multiply_prime(1) == False
    assert is_multiply_prime(2) == False
    assert is_multiply_prime(3) == False
    assert is_multiply_prime(4) == False

def test_is_multiply_prime_small_products():
    assert is_multiply_prime(12) == True  # 2*2*3
    assert is_multiply_prime(18) == True  # 2*3*3
    assert is_multiply_prime(20) == True  # 2*2*5
    assert is_multiply_prime(28) == True  # 2*2*7
    assert is_multiply_prime(44) == True  # 2*2*11
    assert is_multiply_prime(50) == True  # 2*5*5

def test_is_multiply_prime_larger_products():
    assert is_multiply_prime(105) == True  # 3*5*7
    assert is_multiply_prime(154) == True  # 2*7*11
    assert is_multiply_prime(286) == True  # 2*11*13
    assert is_multiply_prime(210) == False  # 2*3*5*7 is 4 primes, not 3

def test_is_multiply_prime_non_products():
    assert is_multiply_prime(5) == False
    assert is_multiply_prime(7) == False
    assert is_multiply_prime(11) == False
    assert is_multiply_prime(13) == False
    assert is_multiply_prime(9) == False   # 3*3 is only 2 primes
    assert is_multiply_prime(15) == False  # 3*5 is only 2 primes
    assert is_multiply_prime(21) == False  # 3*7 is only 2 primes
    assert is_multiply_prime(25) == False  # 5*5 is only 2 primes

def test_is_multiply_prime_edge_cases():
    assert is_multiply_prime(0) == False
    assert is_multiply_prime(-1) == False
    assert is_multiply_prime(-30) == False

@pytest.mark.parametrize("input_val,expected", [
    (8, True),    # 2*2*2
    (12, True),   # 2*2*3
    (18, True),   # 2*3*3
    (20, True),   # 2*2*5
    (27, True),   # 3*3*3
    (28, True),   # 2*2*7
    (30, True),   # 2*3*5
    (44, True),   # 2*2*11
    (45, True),   # 3*3*5
    (50, True),   # 2*5*5
    (52, True),   # 2*2*13
    (63, True),   # 3*3*7
    (68, True),   # 2*2*17
    (75, True),   # 3*5*5
    (76, True),   # 2*2*19
    (92, True),   # 2*2*23
    (98, True),   # 2*7*7
    (99, True),   # 3*3*11
    (116, True),  # 2*2*29
    (117, True),  # 3*3*13
    (124, True),  # 2*2*31
    (147, True),  # 3*7*7
    (148, True),  # 2*2*37
    (153, True),  # 3*3*17
    (164, True),  # 2*2*41
    (171, True),  # 3*3*19
    (172, True),  # 2*2*43
    (175, True),  # 5*5*7
    (188, True),  # 2*2*47
    (207, True),  # 3*3*23
    (236, True),  # 2*2*59
    (244, True),  # 2*2*61
    (261, True),  # 3*3*29
    (268, True),  # 2*2*67
    (275, True),  # 5*5*11
    (279, True),  # 3*3*31
    (284, True),  # 2*2*71
    (316, True),  # 2*2*79
    (325, True),  # 5*5*13
    (332, True),  # 2*2*83
    (333, True),  # 3*3*37
    (356, True),  # 2*2*89
    (363, True),  # 3*11*11
    (369, True),  # 3*3*41
    (387, True),  # 3*3*43
    (425, True),  # 5*5*17
    (475, True),  # 5*5*19
    (507, True),  # 3*13*13
    (531, True),  # 3*3*59
    (539, True),  # 7*7*11
    (575, True),  # 5*5*23
    (603, True),  # 3*3*67
    (637, True),  # 7*7*13
    (725, True),  # 5*5*29
    (775, True),  # 5*5*31
    (847, True),  # 7*11*11
    (867, True),  # 3*17*17
    (931, True),  # 7*7*19
    (1075, True), # 5*5*43
    (1183, True)  # 7*13*13
])
def test_is_multiply_prime_parametrized(input_val, expected):
    assert is_multiply_prime(input_val) == expected