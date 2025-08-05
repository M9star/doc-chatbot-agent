from .validators import validate_email, validate_phone, parse_date, validate_name

def collect_user_info():
    print("Let's book your appointment. Please provide the following information:")
    while True:
        name = input("Name: ").strip()
        if validate_name(name):
            break
        print("Invalid name. Please enter a valid name (letters and spaces only).")
    while True:
        phone = input("Phone Number: ").strip()
        if validate_phone(phone):
            break
        print("Invalid phone number. Please enter a valid 10-digit number (with optional country code).")
    while True:
        email = input("Email: ").strip()
        if validate_email(email):
            break
        print("Invalid email format. Please try again.")
    while True:
        date_input = input("Preferred Appointment Date (e.g., 'Next Monday', '2025-08-10'): ").strip()
        date_str = parse_date(date_input)
        if date_str:
            break
        print("Could not parse date. Please try again (e.g., 'Next Monday', '2025-08-10').")
    print(f"\nThank you, {name}! Your appointment is booked for {date_str}.")
    return {
        "name": name,
        "phone": phone,
        "email": email,
        "date": date_str
    }
