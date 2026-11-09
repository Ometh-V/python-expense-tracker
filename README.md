# Expense Tracker

#### Video Demo: https://youtu.be/ZzBb97QDwZs

## Description

This Expense Tracker is a Python-based command-line application designed to help users efficiently manage and analyze their personal expenses. Users can add new expenses, view past expenses with filtering options, analyze their spending habits, and export data for further use. The program leverages CSV files for data storage, ensuring simplicity and portability.

## Features

- **Add Expenses**: Users can input expenses along with a date and category.
- **View Expenses**: Expenses can be displayed with filtering options (by date, category, or both).
- **Analyze Expenses**: Provides total spending, category breakdown, and highest/lowest expenses.
- **Data Validation**: Ensures categories match correctly and dates are valid.
- **Testing with Pytest**: Includes test cases for validation and date input functions.

## Files in This Project

### `project.py`

- **`main()`**: The entry point of the application that displays the menu.
- **`add_expense()`**: Collects and saves user input into `expenses.csv`.
- **`view_expenses()`**: Reads and displays expenses with filtering capabilities.
- **`analyze_expenses()`**: Analyzes expenses, summarizing key statistics.
- **`validate()`**: Ensures entered dates and categories exist in the dataset.
- **`get_date()`**: Manages date input, allowing default selection of today’s date.

### `test_project.py`

- Unit tests for `validate()` and `get_date()` using **pytest**.
- Mocks user input using `monkeypatch` for automated testing.

### `requirements.txt`

- Lists dependencies (`tabulate`, `pytest`, `datetime`) required for running the project.

## Design Decisions

- **CSV-based storage**: Chosen for its simplicity and accessibility.
- **Filtering before viewing**: Allows users to quickly narrow down their search.
- **Auto-matching categories**: Enhances user experience by reducing input errors.
- **Testing with Pytest**: Ensures robustness and reliability of the core functions.

## How to Run

1. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
2. Run the program:
   ```sh
   python project.py
   ```
3. Follow the on-screen menu options to add, view, or analyze expenses.

## Future Improvements

- **Edit/Delete Expenses**: Allow users to modify existing records.
- **Monthly Reports**: Generate automatic summaries per month.
- **Graphical Interface**: Convert to a GUI-based expense tracker.

This project demonstrates structured programming, data validation, and automated testing, making it a solid foundation for further enhancements!

