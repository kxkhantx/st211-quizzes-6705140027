# Lab 2: Unit Testing Fundamentals & Best Practices

This lab introduces fundamental concepts of unit testing with `pytest`, emphasizing test independence, descriptive naming conventions, boundary value analysis, exception handling, and separating positive from negative test cases.

---

## 📁 Directory Structure

```text
lab2/
├── bank.py               # BankAccount class implementation
├── grades.py             # letter_grade conversion function
├── validators.py         # Email and age input validators
├── test_bad_example.py   # Anti-pattern: chained multi-action test
├── test_dependent.py     # Independent, isolated test cases
├── test_bank.py          # Basic assertion on deposit functionality
├── test_named.py         # Descriptively named test cases covering edge cases
├── test_grades.py        # Boundary value analysis & exception testing
├── test_valid.py         # Positive (happy path) tests for validators
├── test_invalid.py       # Negative (error path) tests using pytest.raises
└── README.md             # Lab documentation
```

---

## 📦 Source Code Overview

### 1. `bank.py` (`BankAccount`)
A bank account class managing balance transactions:
- `__init__(balance=0)`: Initializes account balance.
- `deposit(amount)`: Adds funds; raises `ValueError` if `amount <= 0`.
- `withdraw(amount)`: Subtracts funds; raises `ValueError` if `amount > balance`.

### 2. `grades.py` (`letter_grade`)
Converts numeric scores (0–100) to letter grades:
- `80` to `100`: `"A"`
- `70` to `79`: `"B"`
- `60` to `69`: `"C"`
- `0` to `59`: `"F"`
- Raises `ValueError` for out-of-range scores (`< 0` or `> 100`).

### 3. `validators.py`
Input validation utility functions:
- `validate_email(email)`: Ensures `"@"` is present in email string; raises `ValueError` otherwise.
- `validate_age(age)`: Ensures `age >= 18`; raises `ValueError` for minors under 18.

---

## 🎯 Key Testing Concepts & Patterns

### 1. Test Independence vs. Anti-Patterns
- **Anti-Pattern (`test_bad_example.py`)**: `test_everything_at_once` combines deposit, withdraw, and multiple state changes into one long test. If an assertion fails, subsequent behavior is masked, making root-cause debugging harder.
- **Best Practice (`test_dependent.py`)**: Tests are split into isolated, independent units (`test_deposit_independent` and `test_withdraw_independent`). Each test initializes a clean instance with fresh state.

### 2. Descriptive Test Naming (`test_named.py`)
Tests should clearly describe the condition under test and the expected outcome:
- `test_deposit_increases_balance`: Verifies standard deposit behavior.
- `test_deposit_negative_amount_raises_error`: Verifies rejection of negative deposits.
- `test_withdraw_more_than_balance_raises_error`: Verifies overdraft protection.
- `test_withdraw_exact_balance_leaves_zero`: Verifies boundary case where balance becomes zero.

### 3. Boundary Value Analysis (`test_grades.py`)
- **Boundary transitions**: Tests transition points between letter grades (e.g., 80 vs 79, 60 vs 59).
- **Extreme limits**: Tests exact upper and lower bounds (0 and 100).
- **Invalid boundaries**: Tests values immediately outside the valid range (-1 and 101).

### 4. Exception Testing with `pytest.raises`
Using pytest's `pytest.raises` context manager to assert expected exceptions:
```python
with pytest.raises(ValueError):
    letter_grade(-1)
```
Used across `test_grades.py`, `test_invalid.py`, and `test_named.py`.

### 5. Positive vs. Negative Testing Separation
- **`test_valid.py`**: Focuses purely on valid inputs and expected successful return values (`assert ... is True`).
- **`test_invalid.py`**: Focuses purely on invalid inputs and confirms appropriate error handling.

---

## 🚀 Running the Tests

### Prerequisites
Activate your virtual environment or install `pytest`:
```bash
pip install pytest
```

### 1. Run All Tests
Execute all tests within the `lab2` directory:
```bash
pytest -v
```

Expected output:
```text
test_bad_example.py::test_everything_at_once PASSED                      [  6%]
test_bank.py::test_deposit_increases_balance PASSED                      [ 13%]
test_dependent.py::test_deposit_independent PASSED                       [ 20%]
test_dependent.py::test_withdraw_independent PASSED                      [ 26%]
test_grades.py::test_grade_boundaries PASSED                             [ 33%]
test_grades.py::test_grade_extremes PASSED                               [ 40%]
test_grades.py::test_invalid_scores PASSED                               [ 46%]
test_invalid.py::test_invalid_email PASSED                               [ 53%]
test_invalid.py::test_invalid_age PASSED                                 [ 60%]
test_named.py::test_deposit_increases_balance PASSED                     [ 66%]
test_named.py::test_deposit_negative_amount_raises_error PASSED          [ 73%]
test_named.py::test_withdraw_more_than_balance_raises_error PASSED       [ 80%]
test_named.py::test_withdraw_exact_balance_leaves_zero PASSED            [ 86%]
test_valid.py::test_valid_email PASSED                                   [ 93%]
test_valid.py::test_valid_age PASSED                                     [100%]

============================= 15 passed in 0.04s ==============================
```

### 2. Run Specific Test Files
- **Bank account tests:**
  ```bash
  pytest test_named.py test_bank.py
  ```

- **Grade calculation tests:**
  ```bash
  pytest test_grades.py
  ```

- **Validation tests:**
  ```bash
  pytest test_valid.py test_invalid.py
  ```
