from database.db_manager import DatabaseManager
from models.expense import Expense
from utils.category_factory import CategoryFactory
from services.currency_converter import CurrencyConverter, LiveRateStrategy

class ExpenseManager:
    def __init__(self):
        self.db = DatabaseManager()
        self.converter = CurrencyConverter(LiveRateStrategy())

    def add_expense(self, amount, category_name, date):
        category = CategoryFactory.create_category(category_name)
        expense = Expense(amount, category, date)

        self.db.save_expense(expense)
        print("Expense added successfully.")

    def view_expenses(self):
        expenses = self.db.get_all_expenses()

        if not expenses:
            print("No expenses found.")
            return

        for expense in expenses:
            print(
                f"ID: {expense[0]}, Amount: {expense[1]}, "
                f"Category: {expense[2]}, Date: {expense[3]}"
            )

    def delete_expense(self, expense_id):
        self.db.delete_expense(expense_id)
        print("Expense deleted successfully.")

    def calculate_total(self):
        expenses = self.db.get_all_expenses()
        return sum(float(expense[1]) for expense in expenses)

    def convert_total(self, currency):
        total = self.calculate_total()
        return self.converter.convert(total, currency)
