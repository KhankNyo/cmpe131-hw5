import pytest;
from src.pricing import parse_price;

def test_parse_price():
    valid = ["$1,234.50", "12.5", "$0.99"];
    expected_valid = [1234.5, 12.5, 0.99];
    invalid = ["", "abc", "$12,34,56"];

    for index, string in enumerate(valid): 
        assert parse_price(string) == expected_valid[index];

    for string in invalid: 
        with pytest.raises(ValueError):
            parse_price(string);

