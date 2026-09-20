expenses=[]

def add_expense():
    amount= float(input("amount:"))
    category= input("category(food,travel, etc):").strip().lower()
    date= input("date(YYYY-MM-DD)").strip()
    expenses.append({"amount": amount,"category":category,"date":date})
    print("expense added!")

def ViewExpenses():
    if not expenses:
        print("No expenses yet.")
        return
    for i,e in enumerate(expenses,start=1):
        print(f"{i}.{e['date']}| {e['category']}| Rs{e['amount']:.2f}")

def main():
    while True:
        print("\n---Expense Tracker---")
        print("1. Add expense")
        print("2. View expenses")
        print("3. Quit")
        choice= input("Chose an option:")

        if choice=="1":
            add_expense()
        elif choice == "2":
            ViewExpenses()
        elif choice == "3":
            print("goodbye!")
            break
        else:
            print("invalid choice, try again.")

if __name__== "__main__":
    main()
