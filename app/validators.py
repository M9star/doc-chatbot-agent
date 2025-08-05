import re
from datetime import datetime
import dateparser

def validate_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email) is not None

def validate_phone(phone):
    pattern = r"^(\+\d{1,3}[- ]?)?\d{10}$"
    return re.match(pattern, phone) is not None

def parse_date(date_str):
    dt = dateparser.parse(date_str, settings={'PREFER_DATES_FROM': 'future'})
    if dt:
        return dt.strftime('%Y-%m-%d')
    return None

def validate_name(name):
    return bool(name.strip()) and all(x.isalpha() or x.isspace() for x in name)
