from storage import load_expenses, load_savings, save_expenses, save_savings
from tracker import add_expense, add_saving, list_expenses, list_savings, show_total, show_total_savings, show_category_summary, show_category_summary_savings


def show_menu() -> None:
    print("\n==============================")
    print(" Personal Expense Tracker")
    print("==============================")
    print("1) Add Expense")
    print("2) Add Saving")
    print("3) View All Expenses")
    print("4) Total Spending")
    print("5) Category Summary (Expenses)")
    print("6) View Savings")
    print("7) Total Savings")
    print("8) Category Summary (Savings)")
    print("9) Save & Exit")
    print("==============================")


def main() -> None:
    expenses = load_expenses()
    savings =load_savings()

    while True:
        show_menu()
        choice = input("Choose an option (1-9): ").strip()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            add_saving(savings)
        elif choice == "3":
            list_expenses(expenses)
        elif choice == "4":
            show_total(expenses)
        elif choice == "5":
            show_category_summary(expenses)
        elif choice == "6":
            list_savings(savings)
        elif choice == "7":
            show_total_savings(savings)
        elif choice == "8":
            show_category_summary_savings(savings)
        elif choice == "9":
            save_expenses(expenses)
            save_savings(savings)
            print("✅ Saved. Bye!")
            break
        else:
            print("❌ Invalid choice. Please select 1-9.")


if __name__ == "__main__":
    main()