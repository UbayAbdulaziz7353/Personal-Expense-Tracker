import psycopg2
# Singleton database manager
class DatabaseManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseManager, cls).__new__(cls)
            cls._instance.connection = None
        return cls._instance
    # Create database connection if one does not exist
    def connect(self):
        if self.connection is None:
            self.connection = psycopg2.connect(
                host="aws-1-ca-central-1.pooler.supabase.com",
                database="postgres",
                user="postgres.ppjmlshkkajzfcczwkew",
                password="Braveheart$@01012001",
                port="5432"
            )
        return self.connection

    def save_expense(self, expense):
        conn = self.connect()
        cur = conn.cursor()

        cur.execute(
            "INSERT INTO expenses (amount, category, expense_date) VALUES (%s, %s, %s)",
            (expense.amount, expense.category.name, expense.date)
        )

        conn.commit()
        cur.close()

    def get_all_expenses(self):
        conn = self.connect()
        cur = conn.cursor()

        cur.execute(
            "SELECT id, amount, category, expense_date FROM expenses ORDER BY id"
        )

        expenses = cur.fetchall()
        cur.close()

        return expenses

    def delete_expense(self, expense_id):
        conn = self.connect()
        cur = conn.cursor()

        cur.execute(
            "DELETE FROM expenses WHERE id = %s",
            (expense_id,)
        )

        conn.commit()
        cur.close()
