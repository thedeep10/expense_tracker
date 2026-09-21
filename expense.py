import sqlite3
from datetime import date, datetime

DB_NAME = "expenses.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def init_db():
    with get_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                amount REAL NOT NULL,
                category TEXT NOT NULL,
                date TEXT NOT NULL
            )
        """)


def get_amount():
    while True:
        try:
            amount = float(input("Amount: "))
            if amount <= 0:
                print("Amount must be greater than 0.")
                continue
            return amount
        except ValueError:
            print("Please enter a valid number.")


def get_date():
    while True:
        text = input("Date (YYYY-MM-DD, blank for today): ").strip()
        if text == "":
            return date.today().isoformat()
        try:
            datetime.strptime(text, "%Y-%m-%d")
            return text
        except ValueError:
            print("Use the format YYYY-MM-DD, e.g. 2026-09-20.")


def add_expense():
    amount = get_amount()
    category = input("Category (food, travel, etc.): ").strip().lower()
    if not category:
        category = "other"
    date_text = get_date()

    with get_connection() as conn:
        conn.execute(
            "INSERT INTO expenses (amount, category, date) VALUES (?, ?, ?)",
            (amount, category, date_text),
        )
    print("Expense added!")


def view_expenses():
    with get_connection() as conn:
        rows = conn.execute(
            "SELECT id, date, category, amount FROM expenses ORDER BY date"
        ).fetchall()

    if not rows:
        print("No expenses yet.")
        return
    for id_, date_text, category, amount in rows:
        print(f"{id_}. {date_text} | {category} | ₹{amount:.2f}")


def main():
    init_db()
    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add expense")
        print("2. View expenses")
        print("3. Quit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()