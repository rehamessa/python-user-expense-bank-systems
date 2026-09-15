# Python Fundamentals Projects
 

 
Each project simulates a small "database" using in-memory Python data structures (lists of dictionaries) and includes its own testing section demonstrating both successful and failed scenarios.
 

 
### 1. User Registration System
`user_registration.py`
 
A simple user registration system with custom validation logic.
 
- Validates name (minimum length), email (basic format check), and password (length, uppercase, digit requirements)
- Raises descriptive `ValueError`s for invalid input
- Prevents duplicate email registrations
- Tracks successful registrations in `registered_users` and failed attempts in `failed_registrations`
**Core functions:** `validate_name()`, `validate_email()`, `validate_password()`, `validate_user_data()`, `create_user_account()`
 
### 2. Expense Tracking System
`expense_tracker.py`
 
A simple expense tracker that stores, totals, and summarizes expenses.
 
- Validates that expense amounts are greater than 0
- Stores each expense as a dictionary with amount, category, and description
- Calculates total expenses overall and by category
- Displays all stored expenses in a readable format
**Core functions:** `add_expense()`, `calculate_total_expenses()`, `calculate_total_by_category()`, `show_expenses()`
 
### 3. Mini Banking System
`mini_banking_system.py`
 
A simple banking system supporting account creation, deposits, withdrawals, and transaction history.
 
- Prevents duplicate account names and negative initial balances
- Validates deposit/withdrawal amounts and prevents overdrafts
- Tracks every transaction (`Deposit` / `Withdrawal`) per account
- Displays a full account summary including balance and transaction history
**Core functions:** `create_account()`, `deposit()`, `withdraw()`, `show_account()`
 

## Usage
 
Each project is self-contained in its own file and can be run independently:
 
```bash
python user_registration.py
python expense_tracker.py
python mini_banking_system.py
```
 
Each script includes a testing section at the bottom that runs through valid and invalid scenarios and prints the results.
 
## What These Projects Practice
 
- Functions and clean function design (single responsibility, docstrings)
- Data modeling with lists and dictionaries
- Input validation logic
- Custom exception handling with `raise` and `try/except`
- Structured, readable script organization

 
These projects are for educational and personal practice purposes.
 
