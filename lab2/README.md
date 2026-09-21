# Lab 2: A Beginner's Guide to Software Testing

Welcome! If you have never written a line of code in your life, you are in the right place. 

This folder contains a collection of simple Python programs alongside **automated tests**. Think of automated tests as digital quality-assurance inspectors that check our work to ensure everything works safely, accurately, and as expected.

---

## 💡 What is Software Testing? (The Real-World Analogy)

Imagine a car factory:
- Before a new car is sold, safety engineers test the **brakes**, **headlights**, and **seatbelts**.
- They test the car under normal conditions (driving on a sunny day) and stressful conditions (slamming the brakes on ice).
- If something breaks, they fix it in the factory *before* a customer drives it.

In computer programming, **unit testing** does the exact same thing:
1. We write a small piece of code (like a digital bank account).
2. We write a **test** that gives the code instructions and checks: *"Did the code produce the exact result we expected?"*
3. If the test passes, we know our code is reliable!

In this project, we use a popular Python tool called **pytest** to run all our safety checks automatically in less than a second.

---

## 📂 What is Inside This Folder?

Here is a quick map of the files:

| File Name | What is it? | Plain English Explanation |
| :--- | :--- | :--- |
| **`bank.py`** | 🏦 Program | A digital bank account that lets you deposit, withdraw, and check your money. |
| **`grades.py`** | 🎓 Program | A school grading calculator that turns test scores (like 85) into letter grades (like "A"). |
| **`validators.py`** | 🛡️ Program | A digital security guard that checks if email addresses and ages are valid. |
| **`test_bank.py`** | 🧪 Test | Checks that depositing money into a bank account actually increases the balance. |
| **`test_named.py`** | 🧪 Test | Tests the bank account thoroughly using clearly named, easy-to-read tests. |
| **`test_bad_example.py`** | ⚠️ Lesson | Shows a **poor way** to test code (cramming too many actions into one test). |
| **`test_dependent.py`** | ✨ Lesson | Shows the **correct way** to test code (testing one isolated action at a time). |
| **`test_grades.py`** | 🧪 Test | Checks that the grading calculator works for normal scores, boundary scores, and invalid scores. |
| **`test_valid.py`** | 🧪 Test | Checks the "Happy Path" (valid inputs like an adult's age or a proper email). |
| **`test_invalid.py`** | 🧪 Test | Checks the "Error Path" (making sure bad inputs trigger a proper warning). |

---

## 🔍 How the Programs Work

### 1. The Bank Account (`bank.py`)
A digital wallet with built-in safety rules:
- **Deposit**: Adds money to your balance.
  - *Safety Rule*: You cannot deposit $0 or negative money (e.g. depositing -$50 makes no sense!).
- **Withdraw**: Takes money out of your balance.
  - *Safety Rule*: You cannot take out more money than you currently have (no overdrawing).

### 2. The Grade Calculator (`grades.py`)
Turns a test score from `0` to `100` into a letter grade:
- **80 to 100** = **A**
- **70 to 79** = **B**
- **60 to 69** = **C**
- **0 to 59** = **F**
- *Safety Rule*: If someone enters an impossible score (like `-5` or `150`), the program rejects it and raises an error.

### 3. The Form Validators (`validators.py`)
Acts like a bouncer at a door checking IDs:
- **Email Validator**: Makes sure the email address has an `@` symbol (like `user@example.com`).
- **Age Validator**: Makes sure a person is at least 18 years old.

---

## 🧠 Core Testing Lessons (Explained Simply)

### Lesson 1: Test One Thing at a Time
- **The Bad Way (`test_bad_example.py`)**:
  Imagine testing a car by turning on the radio, accelerating to 60 mph, honking the horn, and rolling down the window all at once. If an alarm goes off, *which part failed?* You have no idea.
- **The Good Way (`test_dependent.py`)**:
  Start each test with a clean, fresh setup. Test deposits alone. Test withdrawals alone. If a test fails, you know the exact culprit immediately.

### Lesson 2: Give Tests Clear, Descriptive Names (`test_named.py`)
Instead of naming a test `test_1()` or `test_stuff()`, we name tests like full sentences:
- `test_deposit_increases_balance`
- `test_deposit_negative_amount_raises_error`
- `test_withdraw_more_than_balance_raises_error`
- `test_withdraw_exact_balance_leaves_zero`

If a test fails at 2:00 AM, the name immediately tells anyone on the team what broke without having to decipher the code!

### Lesson 3: Test the Edges and Boundaries (`test_grades.py`)
Bugs love hiding at the borders! For example:
- A score of `80` is an **A**.
- A score of `79` is a **B**.
Testing both `80` and `79` ensures our code doesn't make an "off-by-one" mistake. We also test absolute limits like `0` (lowest score) and `100` (highest score).

### Lesson 4: Make Sure Bad Inputs Cause Safe Errors (`pytest.raises`)
Good programs do not crash silently or freeze when someone types the wrong thing. They wave a red flag (an "Error" or "Exception").
In our tests, we intentionally supply bad inputs (such as score `-1` or age `17`) to confirm that the program catches them and raises a safe, expected error.

### Lesson 5: Test Both Success and Failure
- **Positive Testing (`test_valid.py`)**: Verifies that when users do the right thing (valid email, age 18), everything succeeds.
- **Negative Testing (`test_invalid.py`)**: Verifies that when users make a mistake (invalid email, age 17), the program catches it.

---

## 🚀 How to Run the Tests Yourself

You don't need any programming skills to run these checks. You only need a terminal (command prompt).

### Step 1: Open your terminal in this `lab2` folder

### Step 2: Run pytest
Type this command and press **Enter**:
```bash
pytest -v
```

*(The `-v` stands for "verbose", meaning "tell me all the details").*

### Step 3: Understanding the Results

When pytest finishes, you will see a checklist on your screen:

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

- **`PASSED` (in Green)**: The test passed! The program behaved exactly as expected.
- **`[ 100% ]`**: Progress counter showing that all 15 safety checks were executed.
- **`15 passed in 0.04s`**: All 15 tests completed successfully in four hundredths of a second.
