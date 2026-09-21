import pytest
from validators import validate_email, validate_age

def test_invalid_email():
    with pytest.raises(ValueError):
        validate_email("invalid-email")

def test_invalid_age():
    with pytest.raises(ValueError):
        validate_age(17)
