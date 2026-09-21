from validators import validate_email, validate_age

def test_valid_email():
    assert validate_email("user@example.com") is True

def test_valid_age():
    assert validate_age(18) is True
