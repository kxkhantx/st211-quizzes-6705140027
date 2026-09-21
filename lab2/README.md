# Lab 2 – Writing Effective Test Cases

## Student Information
- **Name:** Kaung Khant Htoo
- **Student ID:** 6705140027
- **Course:** 192-211 Automated Software Testing
- **Assignment:** Lab 2 – Writing Effective Test Cases

---

## Introduction
This repository contains the laboratory work for **Lab 2 – Writing Effective Test Cases** in the *192-211 Automated Software Testing* course. The purpose of this lab is to develop hands-on skills in writing maintainable, reliable, and well-structured unit tests in Python using the **pytest** testing framework.

Through practical exercises, the lab explores standard testing principles, demonstrating both anti-patterns to avoid and best practices to adopt when designing unit test suites.

---

## Learning Objectives
The primary objectives of this lab are to practice and apply:
- **The AAA (Arrange, Act, Assert) Pattern:** Structuring test functions into distinct phases to enhance readability and traceability.
- **Test Independence:** Ensuring each test case executes in complete isolation with a fresh state, avoiding inter-test dependencies.
- **Boundary Value Testing:** Designing test cases that evaluate inputs at the boundaries of equivalence partitions, extreme values, and invalid thresholds.
- **Descriptive Test Naming:** Using clear, behavior-driven test function names that describe the condition under test and the expected result.
- **Positive and Negative Testing:** Verifying both normal (happy path) execution and proper error handling (such as expecting specific exceptions) for invalid inputs.

---

## Project Structure

```text
lab2/
├── .gitignore              # Specifies files and directories ignored by Git
├── bank.py                 # Implementation of BankAccount class
├── grades.py               # Implementation of letter_grade conversion function
├── validators.py           # Email and age validation utility functions
├── test_bank.py            # Basic unit test verifying BankAccount deposit logic
├── test_bad_example.py     # Anti-pattern demonstration: interdependent, multi-step test
├── test_dependent.py       # Refactored tests demonstrating test independence
├── test_named.py           # Tests demonstrating descriptive naming and edge cases
├── test_grades.py          # Boundary value analysis and exception tests for grading
├── test_valid.py           # Positive test cases verifying valid inputs
└── test_invalid.py         # Negative test cases verifying error handling
```

### File Descriptions
- `bank.py`: Defines the `BankAccount` class with `deposit()` and `withdraw()` operations, enforcing constraints such as positive deposits and overdraft protection.
- `grades.py`: Implements the `letter_grade()` function, mapping percentage scores (0–100) to corresponding letter grades (`A`, `B`, `C`, `F`) and rejecting out-of-range values.
- `validators.py`: Provides input validation functions `validate_email()` and `validate_age()` that enforce basic data requirements.
- Test files (`test_*.py`): Contain unit test suites created to demonstrate specific testing strategies and patterns.

---

## Testing Sections

### Section 1: AAA Pattern & Basic Assertions (`bank.py`, `test_bank.py`)
Focuses on the foundational structure of a unit test using the **Arrange, Act, Assert** pattern:
- **Arrange:** Instantiate a `BankAccount` with an initial balance of 100.
- **Act:** Perform a deposit of 50.
- **Assert:** Verify that the returned balance equals 150.

### Section 2: Test Independence vs. Chained Tests (`test_bad_example.py`, `test_dependent.py`)
- `test_bad_example.py` illustrates a common testing anti-pattern: chaining deposits and withdrawals sequentially within a single test. If an intermediate step fails, subsequent logic is never evaluated, obscuring the root cause.
- `test_dependent.py` demonstrates the correct approach: decomposing operations into separate, isolated tests (`test_deposit_independent` and `test_withdraw_independent`), each beginning with fresh test state.

### Section 3: Descriptive & Behavioral Test Naming (`test_named.py`)
Emphasizes clear naming conventions that reflect specific behaviors and expected outcomes rather than generic names. Covers standard and exceptional bank account behaviors:
- `test_deposit_increases_balance`
- `test_deposit_negative_amount_raises_error`
- `test_withdraw_more_than_balance_raises_error`
- `test_withdraw_exact_balance_leaves_zero`

### Section 4: Boundary Value Testing & Exception Handling (`grades.py`, `test_grades.py`)
Evaluates the `letter_grade` function across boundary points and exception conditions:
- **Partition Boundaries:** Testing scores at cutoff edges (e.g., 80 for 'A', 79 for 'B', 60 for 'C', 59 for 'F').
- **Extreme Limits:** Testing minimum valid score (0) and maximum valid score (100).
- **Exception Verification:** Using `pytest.raises(ValueError)` to verify that invalid scores (`-1`, `101`) trigger appropriate exceptions.

### Section 5: Positive and Negative Testing (`validators.py`, `test_valid.py`, `test_invalid.py`)
Separates test logic into two focused test modules:
- `test_valid.py`: Positive testing verifying that valid data (e.g., valid email formatting and age ≥ 18) returns `True`.
- `test_invalid.py`: Negative testing confirming that invalid data (missing `@` symbol or age < 18) raises a `ValueError`.

---

## How to Run

### 1. Set Up and Activate Virtual Environment
Open Windows PowerShell in the `lab2` folder:

```powershell
# Create virtual environment (if not already created)
python -m venv venv

# Activate virtual environment
.\venv\Scripts\Activate.ps1

# Install pytest (if needed)
pip install pytest
```

### 2. Run All Tests
Execute all tests with verbose output:

```powershell
python -m pytest -v
```

### 3. Run Individual Test Files
To run a specific test suite, supply the filename:

```powershell
python -m pytest test_bank.py -v
python -m pytest test_grades.py -v
python -m pytest test_named.py -v
```

---

## Test Results
All unit tests implemented across the test modules were executed and passed successfully during development:
- `test_bad_example.py`: PASSED
- `test_bank.py`: PASSED
- `test_dependent.py`: PASSED
- `test_grades.py`: PASSED
- `test_invalid.py`: PASSED
- `test_named.py`: PASSED
- `test_valid.py`: PASSED

Total: **15 passed tests** with zero failures or errors.

---

## Technologies Used
- **Python** (Programming language)
- **pytest** (Testing framework)
- **Git / GitHub** (Version control and assignment submission)
- **Windows PowerShell** (Execution environment)

