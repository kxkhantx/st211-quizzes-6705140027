# Lab 3 – Automated Software Testing

## Student Information
- **Name:** Kaung Khant Htoo
- **Student ID:** 6705140027
- **Course:** 192-211 Automated Software Testing
- **Assignment:** Lab 3

---

## Introduction
This repository contains the laboratory work for **Lab 3 – Automated Software Testing** in the *192-211 Automated Software Testing* course. The purpose of this lab is to explore advanced features and test organization patterns provided by Python's **pytest** testing framework.

The lab exercises focus on practical test categorization, handling collection-based assertions, controlling test execution using custom markers, managing conditional and unconditional test skips, documenting known defects using expected failures (`xfail`), and enforcing strict configuration rules via `pytest.ini`.

---

## Learning Objectives
Through this laboratory assignment, the following testing concepts are practiced and demonstrated:
- **Testing Shopping Functionality:** Verifying core logic of a data-driven class, including item accumulation, counts, and price calculations.
- **Collection-Based Testing:** Writing assertions for Python collections (lists, dictionaries, sets) to evaluate contents and equality correctly.
- **Pytest Markers:** Categorizing test cases into functional subsets (such as smoke, slow, and regression tests) using custom `@pytest.mark` attributes.
- **Skipping Tests:** Using conditional (`skipif`) and unconditional (`skip`) markers to bypass tests when features are unimplemented or environmental prerequisites are not met.
- **Strict Test Behavior:** Configuring and observing strict marker validation (`--strict-markers`) to catch unregistered or misspelled marker names during test collection.
- **Expected Failures (`xfail`):** Marking known bugs or unstable tests with `@pytest.mark.xfail` so they do not cause build failures while remaining visible in test reports.

---

## Project Structure

```text
lab3/
├── shopping.py            # Implementation of the ShoppingCart class
├── test_shopping.py       # Test suite for ShoppingCart operations
├── test_collections.py    # Unit tests evaluating lists, dictionaries, and sets
├── test_markers.py        # Test cases categorized using custom pytest markers
├── test_skips.py          # Demonstrations of unconditional and conditional test skips
├── test_strict.py         # Test case demonstrating strict-marker validation
├── test_xfail.py          # Test cases demonstrating expected failure handling
├── pytest.ini             # Pytest configuration file with test options and marker definitions
└── .gitignore             # Specifies untracked files and cache directories to ignore
```

### File Descriptions
- `shopping.py`: Implements a basic `ShoppingCart` class with methods to add items, calculate total cost, and retrieve the item count.
- `test_shopping.py`: Contains a test class (`TestShoppingCart`) testing initialization, item additions, item counts, and total price calculation.
- `test_collections.py`: Tests assertions on lists, dictionaries, and set operations.
- `test_markers.py`: Demonstrates the application of custom tags (`smoke`, `slow`, `regression`) to categorize tests for targeted execution.
- `test_skips.py`: Illustrates unconditional skipping for pending features and version-dependent conditional skipping (`sys.version_info`).
- `test_strict.py`: Contains an intentionally unregistered marker to demonstrate how pytest detects unregistered markers under strict mode.
- `test_xfail.py`: Demonstrates expected failures (`xfail`) for known issues as well as unexpected passes (`xpass`).
- `pytest.ini`: Central configuration file managing pytest discovery paths, CLI flags, registered markers, and test naming patterns.

---

## Testing Topics

### 1. Shopping Tests (`shopping.py`, `test_shopping.py`)
Evaluates the `ShoppingCart` class using class-based test organization:
- `test_new_cart_is_empty`: Validates that a new cart initializes with an item count of 0.
- `test_new_cart_total_is_zero`: Confirms that an empty cart has an initial total of 0.
- `test_add_item_increases_count`: Verifies that adding an item increments the cart's item count.
- `test_total_sums_prices`: Verifies that adding multiple items correctly sums their prices.

### 2. Collection Tests (`test_collections.py`)
Demonstrates how pytest asserts equality and contents across standard Python data structures:
- **Lists:** Testing exact equality and order-independent comparison using `sorted()`.
- **Dictionaries:** Verifying key-value equality regardless of insertion or key ordering.
- **Sets:** Testing set operations such as set intersection (`&`).

### 3. Pytest Markers (`test_markers.py`)
Uses `@pytest.mark` decorators to assign meaningful categories to test functions:
- `@pytest.mark.smoke`: Flags critical test paths (e.g., login, checkout).
- `@pytest.mark.slow`: Identifies time-consuming operations (e.g., report generation).
- `@pytest.mark.regression`: Tags tests verifying that previously fixed defects do not reappear.

### 4. Skipped Tests (`test_skips.py`)
Shows how to temporarily bypass test execution:
- `@pytest.mark.skip(reason=...)`: Unconditionally skips tests for features still in development.
- `@pytest.mark.skipif(condition, reason=...)`: Conditionally evaluates an expression (such as Python version checks) before deciding whether to run or skip the test.

### 5. Strict Testing (`test_strict.py`)
Demonstrates strict marker enforcement configured in `pytest.ini`:
- `test_strict.py` uses an unregistered marker (`@pytest.mark.nonexistent_marker`).
- When run under `--strict-markers`, pytest raises a collection error, preventing typos or undeclared markers from silently being ignored.

### 6. Expected-Failure Tests (`test_xfail.py`)
Demonstrates handling known defects using `@pytest.mark.xfail`:
- **XFAIL:** Tests that fail as expected due to known, unresolved issues without breaking the overall test run.
- **XPASS:** Tests marked as expected to fail that unexpectedly pass, alerting developers that an issue may have been fixed.

---

## Configuration (`pytest.ini`)
The `pytest.ini` configuration file sets project-level defaults for pytest:
- **`testpaths = .`**: Specifies the directory to search for tests.
- **`addopts = -v --tb=short --strict-markers`**: Automatically applies verbose output, shortened tracebacks, and strict marker verification on test runs.
- **`markers`**: Explicitly registers custom markers (`smoke`, `slow`, `regression`) with descriptive summaries to satisfy strict marker enforcement.
- **Discovery patterns**: Defines standard naming rules for test files (`python_files = test_*.py`), classes (`python_classes = Test*`), and functions (`python_functions = test_*`).

---

## How to Run

### 1. Environment Setup (Windows PowerShell)
Open PowerShell in the `lab3` folder and activate the virtual environment:

```powershell
# Activate virtual environment (if available)
.\venv\Scripts\Activate.ps1

# Install pytest (if needed)
pip install pytest
```

### 2. Run All Valid Tests
To run the standard test suite while bypassing the strict-marker demonstration file (`test_strict.py`):

```powershell
python -m pytest -v --ignore=test_strict.py
```

### 3. Run Individual Test Files
Individual test files can be executed directly:

```powershell
python -m pytest test_shopping.py -v
python -m pytest test_collections.py -v
python -m pytest test_markers.py -v
python -m pytest test_skips.py -v
python -m pytest test_xfail.py -v
```

### 4. Run Filtered Tests by Marker
Execute specific test categories using the `-m` flag:

```powershell
python -m pytest -m smoke -v --ignore=test_strict.py
python -m pytest -m regression -v --ignore=test_strict.py
```

---

## Test Results
The test suite can be executed directly using pytest from the terminal. During execution, pytest outputs the status of each test:
- Tests that meet all assertions report as **PASSED**.
- Incomplete features or version-gated tests report as **SKIPPED**.
- Known defective features report as **XFAIL** (or **XPASS** if they pass unexpectedly).
- Detailed summaries, execution times, and collection metrics are displayed directly in the terminal upon completion.

---

## Technologies Used
- **Python** – Core programming language
- **pytest** – Automated testing framework
- **Git / GitHub** – Version control and assignment repository
- **Windows PowerShell** – Command-line execution environment


