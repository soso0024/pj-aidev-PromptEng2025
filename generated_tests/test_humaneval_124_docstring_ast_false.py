# Test cases for HumanEval/124
# Generated using Claude API


def valid_date(date):
    """You have to write a function which validates a given date string and
    returns True if the date is valid otherwise False.
    The date is valid if all of the following rules are satisfied:
    1. The date string is not empty.
    2. The number of days is not less than 1 or higher than 31 days for months 1,3,5,7,8,10,12. And the number of days is not less than 1 or higher than 30 days for months 4,6,9,11. And, the number of days is not less than 1 or higher than 29 for the month 2.
    3. The months should not be less than 1 or higher than 12.
    4. The date should be in the format: mm-dd-yyyy

    for example: 
    valid_date('03-11-2000') => True

    valid_date('15-01-2012') => False

    valid_date('04-0-2040') => False

    valid_date('06-04-2020') => True

    valid_date('06/04/2020') => False
    """

    try:
        date = date.strip()
        month, day, year = date.split('-')
        month, day, year = int(month), int(day), int(year)
        if month < 1 or month > 12:
            return False
        if month in [1,3,5,7,8,10,12] and day < 1 or day > 31:
            return False
        if month in [4,6,9,11] and day < 1 or day > 30:
            return False
        if month == 2 and day < 1 or day > 29:
            return False
    except:
        return False

    return True


# Generated test cases:
import pytest

@pytest.mark.parametrize("date,expected", [
    ("03-11-2000", True),
    ("15-01-2012", False),
    ("04-0-2040", False),
    ("06-04-2020", True),
    ("06/04/2020", False),
    ("", False),
    (" ", False),
    ("13-01-2020", False),
    ("00-01-2020", False),
    ("01-32-2020", False),
    ("01-00-2020", False),
    ("04-31-2020", False),
    ("02-30-2020", False),
    ("02-29-2020", True),
    ("02-28-2020", True),
    ("06-30-2020", True),
    ("06-31-2020", False),
    ("abc-12-2020", False),
    ("12-abc-2020", False),
    ("12-12-abcd", False),
    ("12-12-2020-", False),
    ("-12-12-2020", False),
    ("12--12-2020", False),
    ("12-12--2020", False),
    ("1-1-2020", True),
    ("01-1-2020", True),
    ("1-01-2020", True),
    ("11-11-11", True),
    ("11.11.2011", False),
    ("11_11_2011", False)
])
def test_valid_date_parametrized(date, expected):
    assert valid_date(date) == expected

def test_valid_date_none_input():
    assert valid_date(None) == False

def test_valid_date_non_string_input():
    assert valid_date(123) == False
    assert valid_date(12.34) == False
    assert valid_date([]) == False
    assert valid_date({}) == False

def test_valid_date_whitespace():
    assert valid_date("  04-01-2020  ") == True
    assert valid_date("\t04-01-2020\n") == True
    assert valid_date("  ") == False

def test_valid_date_special_months():
    # Test 31-day months
    for month in [1, 3, 5, 7, 8, 10, 12]:
        month_str = f"{month:02d}"
        assert valid_date(f"{month_str}-31-2020") == True
        assert valid_date(f"{month_str}-32-2020") == False
    
    # Test 30-day months
    for month in [4, 6, 9, 11]:
        month_str = f"{month:02d}"
        assert valid_date(f"{month_str}-30-2020") == True
        assert valid_date(f"{month_str}-31-2020") == False

def test_valid_date_february():
    assert valid_date("02-28-2020") == True
    assert valid_date("02-29-2020") == True
    assert valid_date("02-30-2020") == False
    assert valid_date("02-00-2020") == False