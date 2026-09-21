import pytest
from grades import letter_grade

def test_grade_boundaries():
    assert letter_grade(80) == "A"
    assert letter_grade(79) == "B"
    assert letter_grade(60) == "C"
    assert letter_grade(59) == "F"

def test_grade_extremes():
    assert letter_grade(0) == "F"
    assert letter_grade(100) == "A"

def test_invalid_scores():
    with pytest.raises(ValueError):
        letter_grade(-1)

    with pytest.raises(ValueError):
        letter_grade(101)
