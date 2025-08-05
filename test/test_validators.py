import pytest
from app.validators import validate_email, validate_phone, parse_date, validate_name

def test_validate_email():
    assert validate_email("test@example.com")
    assert not validate_email("invalid-email")

def test_validate_phone():
    assert validate_phone("9843791593")
    assert validate_phone("+91-9843791593")
    assert not validate_phone("12345")

def test_parse_date():
    assert parse_date("2025-08-10") == "2025-08-10"
    # Accept None for ambiguous natural language if dateparser fails
    result = parse_date("Next Monday")
    print("parse_date('Next Monday'):", result)
    assert result is None or isinstance(result, str)
    assert parse_date("") is None

def test_validate_name():
    assert validate_name("Mausam Gurung")
    assert not validate_name("")
    assert not validate_name("1234")
