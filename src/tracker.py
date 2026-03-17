from datetime import date
from tabulate import tabulate


def add_expense(expenses: list[dict]) -> None:
    """Ask user details and add a new expense dictionary into the list."""
    print("\nAdd a new expense")

    amount_str = input("Amount (e.g., 120.50): ").strip()
    category = input("Category (e.g., Food/Travel/Rent): ").strip()
    description = input("Description (e.g., Uber Auto): ").strip()

    # Basic validation (beginner-friendly)
    if not amount_str:
        print("❌ Amount cannot be empty.")
        return

    try:
        amount = float(amount_str)
    except ValueError:
        print("❌ Amount must be a number.")
        return

    if amount <= 0:
        print("❌ Amount must be greater than 0.")
        return

    if not category:
        print("❌ Category cannot be empty.")
        return

    expense = {
        "date": str(date.today()),
        "amount": amount,
        "category": category,
        "description": description
    }

    expenses.append(expense)
    print("✅ Expense added successfully!")

def add_saving(savings: list[dict]) -> None:
    """Ask user details and add a new saving dictionary into the list."""
    print("\nAdd a new saving")

    amount_str = input("Amount (e.g., 120.50): ").strip()
    category = input("Category (e.g., Salary/Investment): ").strip()
    description = input("Description (e.g., Monthly Salary): ").strip()

    # Basic validation (beginner-friendly)
    if not amount_str:
        print("❌ Amount cannot be empty.")
        return

    try:
        amount = float(amount_str)
    except ValueError:
        print("❌ Amount must be a number.")
        return

    if amount <= 0:
        print("❌ Amount must be greater than 0.")
        return

    if not category:
        print("❌ Category cannot be empty.")
        return

    saving = {
        "date": str(date.today()),
        "amount": amount,
        "category": category,
        "description": description
    }

    savings.append(saving)
    print("✅ Saving added successfully!")


def list_expenses(expenses: list[dict]) -> None:
    """Print all expenses in a table format."""
    print("\nAll expenses")

    if not expenses:
        print("No expenses found yet.")
        return

    rows = []
    for e in expenses:
        rows.append([e["date"], e["amount"], e["category"], e["description"]])

    print(tabulate(rows, headers=["Date", "Amount", "Category", "Description"], tablefmt="grid"))

def list_savings(savings: list[dict]) -> None:
    """Print all savings in a table format."""
    print("\nAll savings")

    if not savings:
        print("No savings found yet.")
        return

    rows = []
    for s in savings:
        rows.append([s["date"], s["amount"], s["category"], s["description"]])

    print(tabulate(rows, headers=["Date", "Amount", "Category", "Description"], tablefmt="grid"))


def show_total(expenses: list[dict]) -> None:
    """Print total spending."""
    total = 0.0
    for e in expenses:
        total += float(e["amount"])

    print(f"\nTotal spending: ₹{total:.2f}")

def show_total_savings(savings: list[dict]) -> None:
    """Print total saving."""
    total = 0.0
    for s in savings:
        total += float(s["amount"])

    print(f"\nTotal saving: ₹{total:.2f}")


def show_category_summary(expenses: list[dict]) -> None:
    """Print spending summary by category."""
    print("\nCategory summary")

    if not expenses:
        print("No expenses found yet.")
        return

    summary = {}
    for e in expenses:
        cat = e["category"]
        amt = float(e["amount"])
        summary[cat] = summary.get(cat, 0.0) + amt

    rows = []
    for cat, amt in summary.items():
        rows.append([cat, f"₹{amt:.2f}"])

    print(tabulate(rows, headers=["Category", "Total"], tablefmt="grid"))


def show_category_summary_savings(savings: list[dict]) -> None:
    """Print savings summary by category."""
    print("\nSavings Category Summary")

    if not savings:
        print("No savings found yet.")
        return

    summary = {}
    for s in savings:
        cat = s["category"]
        amt = float(s["amount"])
        summary[cat] = summary.get(cat, 0.0) + amt

    rows = []
    for cat, amt in summary.items():
        rows.append([cat, f"₹{amt:.2f}"])

    print(tabulate(rows, headers=["Category", "Total"], tablefmt="grid"))

