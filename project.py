from collections import defaultdict
from datetime import datetime
from tabulate import tabulate
import os
import csv


def main():
    """
    Main function to run the Expense Tracker
    """

    while True:
        print("\n==== Expense Tracker ====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Analyze Expenses")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        match choice:
            case "1":
                add_expense()
            case "2":
                view_expenses()
            case "3":
                analyze_expense()
            case "4":
                print("Exiting... Goodbye!")
                break
            case _:
                print("Invalid choice. Please enter a number from 1 to 5.")


def add_expense():
    """
    Adds an expense to a file
    """

    print("\n==== Add Expenses ====")
    try:
        amount = float(input("Enter amount: ").strip())
        category = input("Enter category: ").strip().lower()
        date = get_date()

        # Set default category if empty
        if not category or category == "misc":
            category = "Miscellaneous"

        initialize_file()

        with open("expenses.csv", "a") as file:
            file.write(f"{date},{category.lower()},{amount}\n")

        print("===== Expense Added Successfully =====")

    except ValueError:
        print("Invalid Expense! Please enter a valid number")
        add_expense()


def view_expenses(file_name="expenses.csv"):
    """
    Enables user to view expenses
    """
    while True:
        try:
            with open(file_name) as file:
                reader = csv.reader(file)
                header = next(reader, None)
                expenses = list(reader)

                if not header or not expenses:
                    print("No records yet")
                    return

                print("\n==== Filter expenses ====")
                print("1. Filter by Date")
                print("2. Filter by Category")
                print("3. Filter by Both")
                print("0. Go Back")

                choice = input("Enter your choice: ").strip()

                if choice == "1":
                    date = get_date()
                    if not validate(date, 0, expenses):
                        print(f"No expenses on {date}")
                        continue
                    filtered_expenses = [row for row in expenses if row[0] == date]

                elif choice == "2":
                    category = input("Enter Category to filter: ").strip().lower()
                    if not validate(category, 1, expenses):
                        print(f"No expenses in {category} category")
                        continue
                    if category == "misc":
                        category = "miscellaneous"
                    filtered_expenses = [row for row in expenses if row[1] == category]

                elif choice == "3":
                    date = get_date()
                    category = input("Enter Category to filter: ").strip().lower()
                    if not validate(date, 0, expenses):
                        print(f"No expenses on {date}")
                        continue
                    if not validate(category, 1, expenses):
                        print(f"No expenses in {category} category")
                        continue
                    filtered_expenses = [
                        row for row in expenses if row[0] == date and row[1] == category
                    ]

                elif choice == "0":
                    return

                else:
                    print("Invalid choice please select 1, 2, 3 or 0")

                print("===== Your Expenses =====")
                print(tabulate(filtered_expenses, headers=header, tablefmt="grid"))
                return
        except FileNotFoundError:
            print(f"The file {file_name} does not exist")
            return
        except Exception as e:
            print(f"An error occurred: {e}")
            return


def analyze_expense(file_name="expenses.csv"):
    """
    Analyze expenses by calculating total spending, category-wise spending,
    and identifying the highest & lowest expenses.
    """
    try:
        with open(file_name) as file:
            reader = csv.reader(file)
            header = next(reader, None)  # Skip header
            expenses = list(reader)

            if not header or not expenses:
                print("No records to analyze.")
                return

            total_spending = 0
            category_totals = defaultdict(float)
            highest_expense = ("", 0)  # (Category, Amount)
            lowest_expense = ("", float("inf"))

            for row in expenses:
                date, category, amount = row[0], row[1], float(row[2])
                total_spending += amount
                category_totals[category] += amount

                # Check highest & lowest expenses
                if amount > highest_expense[1]:
                    highest_expense = (category, amount)
                if amount < lowest_expense[1]:
                    lowest_expense = (category, amount)

            # Format results
            print("\n===== Expense Analysis =====")
            print(f"Total Spending: ${total_spending:.2f}")

            category_table = [
                [cat, f"${amt:.2f}"] for cat, amt in category_totals.items()
            ]
            print("\nSpending by Category:")
            print(
                tabulate(
                    category_table, headers=["Category", "Total Spent"], tablefmt="grid"
                )
            )

            print(
                f"\nHighest Expense: ${highest_expense[1]:.2f} ({highest_expense[0]})"
            )
            print(f"Lowest Expense: ${lowest_expense[1]:.2f} ({lowest_expense[0]})")

    except FileNotFoundError:
        print(f"The file {file_name} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")


def get_date():
    """
    Get a valid date from the user, defaulting to today's date if left blank.
    """
    while True:
        date_str = input("Enter date (YYYY-MM-DD) or press Enter for today: ").strip()

        if not date_str:
            return datetime.today().strftime("%Y-%m-%d")  # Default to today

        try:
            valid_date = datetime.strptime(date_str, "%Y-%m-%d")
            return valid_date.strftime("%Y-%m-%d")  # Return properly formatted date
        except ValueError:
            print(
                "❌ Invalid date format. Please enter date in (YYYY-MM-DD). Try again."
            )
            continue


def initialize_file():
    """
    Initialize the expenses file with headers if it doesn't exist or is empty.
    """

    if not os.path.exists("expenses.csv") or os.stat("expenses.csv").st_size == 0:
        with open("expenses.csv", "w") as file:
            file.write("Date,Category,Amount\n")


def validate(value, index, expenses):
    """
    Check if a given date or category exists in the expenses list.

    Parameters:
    - value (str): The date or category to check.
    - column_index (int): 0 for date, 1 for category.
    - expenses (list): List of expenses loaded from the CSV.

    Returns:
    - bool: True if the value exists, False otherwise.
    """
    if value == "misc":
        value = "miscellaneous"
    return any(row[index] == value.lower() for row in expenses)


if __name__ == "__main__":
    main()
