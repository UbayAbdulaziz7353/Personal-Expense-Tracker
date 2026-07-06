class Expense:
    def __init__(self, amount: float, category, date: str, expense_id=None):
        self.id = expense_id
        self.amount = amount
        self.category = category
        self.date = date
