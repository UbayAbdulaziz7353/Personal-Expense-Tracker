from services.expense_manager import ExpenseManager

def menu():
    manager = ExpenseManager()

    while True:
        print("\nPersonal Expense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Calculate Total Spending")
        print("5. Convert Total Currency")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            amount = float(input("Enter amount: "))

            if amount <= 0:
                print("Amount must be greater than 0.")
                continue

            category = input("Enter category: ").strip()

            if category == "":
                print("Category cannot be empty.")
                continue

            date = input("Enter date (YYYY-MM-DD): ")
            manager.add_expense(amount, category, date)

        elif choice == "2":
            expenses = manager.db.get_all_expenses()

            if len(expenses) == 0:
                print("No expenses found.")
            else:
                manager.view_expenses()

        elif choice == "3":
            expense_id = int(input("Enter expense ID to delete: "))
            manager.delete_expense(expense_id)

        elif choice == "4":
            total = manager.calculate_total()
            print(f"Total spending: {total}")

        elif choice == "5":
            currency = input("Enter target currency: ")
            converted = manager.convert_total(currency)
            print(f"Converted total: {converted:.2f} {currency.upper()}")

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please choose a number from 1 to 6.")

if __name__ == "__main__":
    menu()
