# Product Inventory Management System

A beginner-friendly Python assignment demonstrating functions, input validation, exceptions, logging, automated tests with pytest, and code quality checks with Ruff.

## Features

- `calculate_total_price(price, quantity)`: calculates price multiplied by quantity.
- `apply_discount(total, discount_percent)`: applies a discount from 0% to 100%.
- `check_stock(available_stock, requested_quantity)`: returns `True` if stock is sufficient and `False` otherwise.
- Raises `TypeError` for incorrect input types and `ValueError` for invalid values.
- Writes successful operations and errors to `inventory.log`.
- Includes pytest test cases for valid and invalid inputs.

## Requirements

- macOS
- Python 3.10 or newer

## Setup on macOS

1. Open Terminal and move into this project folder:

   ```bash
   cd ProductInventoryManagement
   ```

2. Create a virtual environment:

   ```bash
   python3 -m venv .venv
   ```

3. Activate it:

   ```bash
   source .venv/bin/activate
   ```

4. Install the required packages:

   ```bash
   python -m pip install -r requirements.txt
   ```

## Run the tests

```bash
python -m pytest -v
```

## Run Ruff checks and formatting

Check for linting issues:

```bash
ruff check .
```

Automatically format Python files:

```bash
ruff format .
```

Check formatting without changing files:

```bash
ruff format --check .
```

Run the checks again after formatting:

```bash
ruff check .
ruff format --check .
```

## Example usage

Run this command from the project folder:

```bash
python -c "from inventory import calculate_total_price, apply_discount, check_stock; total = calculate_total_price(500, 2); print('Total:', total); print('After discount:', apply_discount(total, 10)); print('Stock available:', check_stock(5, 2))"
```

The application creates `inventory.log` when operations are performed. This generated log file is excluded from Git using `.gitignore`.

## GitHub submission

1. Create a new GitHub repository named `ProductInventoryManagement`.
2. Upload `inventory.py`, `test_inventory.py`, `README.md`, `requirements.txt`, and `.gitignore`.
3. Do not upload `.venv`, `__pycache__`, or generated log files.
4. Run pytest and Ruff commands in Terminal and capture screenshots showing the successful results.
5. Submit the repository URL through the assigned classroom platform.

## Expected test coverage

The test suite contains eight tests covering successful calculations, valid discounts, available and insufficient stock, negative values, invalid quantity types, and out-of-range discounts.


Output:

