import pytest;
from src.pricing import *;

@pytest.mark.parametrize("test_input, expected", [
    ("$1,234.50", 1234.5), 
    ("12.5", 12.5), 
    ("$0.99", 0.99)
])
def test_parse_price_valid(test_input, expected):
    assert parse_price(test_input) == expected;

@pytest.mark.parametrize("test_input, expected", [
    ("", ValueError), 
    ("abc", ValueError), 
    ("$12,34,56", ValueError)
])
def test_parse_price_invalid(test_input, expected):
    with pytest.raises(expected):
        parse_price(test_input);

def test_format_currency():
    valid_cases = [12.5, .9, 1.99999]; 
    expected = ["$12.50", "$0.90", "$2.00"];

    for index, value in enumerate(valid_cases):
        assert format_currency(value) == expected[index];

    invalid = ["hello, world", test_format_currency, "some" + "[\"other\"]" * len("junk")];
    for value in invalid:
        with pytest.raises((ValueError, TypeError)):
            format_currency(value);

def test_apply_percent():
    price = 10.0;
    valid_percent = [0.0, 1.0, 50.0, 99.99999];
    expected = [10.0 - 0, 10.0 - 0.1, 10.0 - 5.0, 10.0 - 10.0*valid_percent[-1]*.01];
    invalid_percent = [-1.0, 101.0];

    for index, value in enumerate(valid_percent):
        assert apply_discount(price, value) == expected[index];

    for value in invalid_percent:
        with pytest.raises(ValueError):
            apply_discount(price, value);

def test_add_tax():
    price = 10.0;
    custom_rates = [.11, .2, .99, 1.0];
    assert add_tax(price) == price * (1.07)
    for value in custom_rates:
        assert add_tax(price, value) == price * (1.0 + value)

    with pytest.raises(ValueError):
        add_tax(price, -1);
    with pytest.raises(ValueError):
        add_tax(-1);

def test_bulk_total():
    price_list = [1, 2, 3, 4, 5];
    assert bulk_total(price_list) == sum(price_list)*1.07;


