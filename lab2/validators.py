def validate_email(email):
    if "@" not in email:
        raise ValueError("Invalid email")
    return True

def validate_age(age):
    if age < 18:
        raise ValueError("Must be 18 or older")
    return True
