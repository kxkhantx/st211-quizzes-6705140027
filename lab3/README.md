# Lab 3: Advanced Pytest Configuration & Test Organization

This lab covers essential pytest features for structuring test suites, configuring test discovery and behavior, categorizing tests using custom markers, handling skipped and expected failing tests, and testing common Python collections and classes.

---

## 📁 Directory Structure

```text
lab3/
├── pytest.ini             # Pytest configuration and custom marker definitions
├── shopping.py            # ShoppingCart implementation
├── test_shopping.py       # Class-based tests for ShoppingCart
├── test_collections.py    # Pytest assertions on lists, dicts, and sets
├── test_markers.py        # Custom markers (@pytest.mark.smoke, slow, regression)
├── test_skips.py          # Conditional and unconditional test skipping
├── test_xfail.py          # Expected failures (XFAIL and XPASS)
├── test_strict.py         # Demonstration of --strict-markers error handling
└── README.md              # Lab documentation
```

---

## 🎯 Key Concepts & Files

### 1. Pytest Configuration (`pytest.ini`)
Configures test discovery and execution settings:
- **`testpaths = .`**: Root directory for finding tests.
- **`addopts = -v --tb=short --strict-markers`**: Default CLI options for verbose output, concise tracebacks, and strict marker verification.
- **`markers`**: Registers custom markers (`smoke`, `slow`, `regression`) with descriptions to avoid unregistered marker warnings or collection errors.
- **Naming Conventions**: Standard patterns for test files (`test_*.py`), classes (`Test*`), and functions (`test_*`).

### 2. Class-based Testing (`shopping.py` & `test_shopping.py`)
- **`ShoppingCart`**: Simple shopping cart supporting item additions (`add(name, price)`), total price calculation (`total()`), and item count (`count()`).
- **`TestShoppingCart`**: Groups tests inside a class:
  - `test_new_cart_is_empty`: Validates initial item count is 0.
  - `test_new_cart_total_is_zero`: Validates initial total price is 0.
  - `test_add_item_increases_count`: Verifies adding an item updates the count.
  - `test_total_sums_prices`: Verifies accurate sum of item prices.

### 3. Collection Assertions (`test_collections.py`)
Demonstrates how pytest handles assertions across standard Python data structures:
- **Lists**: Exact equality (`==`) and order-independent matching via `sorted()`.
- **Dictionaries**: Key-value pair equality independent of key ordering.
- **Sets**: Set operations such as intersection (`&`).

### 4. Custom Markers (`test_markers.py`)
Demonstrates organizing tests by category using `@pytest.mark`:
- `@pytest.mark.smoke`: Critical path smoke tests (`test_critical_login`, `test_critical_checkout`).
- `@pytest.mark.slow`: Long-running tests (`test_full_report_generation`).
- `@pytest.mark.regression`: Verification for previously resolved issues (`test_old_bug_stays_fixed`).

### 5. Skipping Tests (`test_skips.py`)
- **Unconditional Skip** (`@pytest.mark.skip(reason=...)`): Skips `test_future_feature` because the feature has not yet been implemented.
- **Conditional Skip** (`@pytest.mark.skipif(condition, reason=...)`): Evaluates conditions at runtime (e.g., checks `sys.version_info < (3, 8)` for `test_needs_modern_python`).

### 6. Expected Failures (`test_xfail.py`)
- `@pytest.mark.xfail(reason=...)`: Marks tests that are expected to fail without failing the test run.
  - **XFAIL**: `test_known_broken_feature` fails assertion as expected.
  - **XPASS**: `test_actually_works_now` passes despite being marked `xfail`, signaling that the underlying issue may have been resolved.

### 7. Strict Markers Demonstration (`test_strict.py`)
- Demonstrates `--strict-markers` defined in `pytest.ini`.
- `test_bad_marker` uses `@pytest.mark.nonexistent_marker`, which has not been registered in `pytest.ini`.
- Pytest halts test collection with an error to safeguard against typos in marker names.

---

## 🚀 Running the Tests

### Prerequisites
Make sure `pytest` is installed in your Python environment:
```bash
pip install pytest
```

### 1. Run the Main Test Suite
Because `test_strict.py` deliberately contains an unregistered marker to showcase strict marker enforcement, exclude it when running the normal test suite:
```bash
pytest --ignore=test_strict.py
```

Expected output:
```text
13 passed, 1 skipped, 1 xfailed, 1 xpassed in 0.08s
```

### 2. Filter Tests by Custom Marker
Run only tests tagged with specific markers using the `-m` flag:

- **Run smoke tests:**
  ```bash
  pytest -m smoke --ignore=test_strict.py
  ```

- **Run regression tests:**
  ```bash
  pytest -m regression --ignore=test_strict.py
  ```

- **Run non-slow tests:**
  ```bash
  pytest -m "not slow" --ignore=test_strict.py
  ```

### 3. Run Specific Test Files
```bash
pytest test_shopping.py
pytest test_collections.py
pytest test_skips.py
pytest test_xfail.py
```

### 4. Verify Strict Markers Enforcement
To see pytest block execution due to unregistered markers:
```bash
pytest test_strict.py
```
This produces:
```text
ERROR collecting test_strict.py
'nonexistent_marker' not found in `markers` configuration option
```
