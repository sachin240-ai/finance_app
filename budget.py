from db import get_db

def create_budget_table():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS budgets (
        user_id INTEGER,
        category TEXT,
        budget_limit REAL,
        PRIMARY KEY(user_id, category)
    )
''')
    conn.commit()

def set_budget(user_id, category, limit):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('''
    INSERT OR REPLACE INTO budgets (user_id, category, budget_limit) VALUES (?, ?, ?)
''', (user_id, category, limit))

def check_budget(user_id, category):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('''
    SELECT budget_limit FROM budgets WHERE user_id=? AND category=?
''', (user_id, category))
    limit_row = cursor.fetchone()

    if limit_row:
        cursor.execute('''
            SELECT SUM(amount) FROM transactions WHERE user_id=? AND category=? AND type='expense'
        ''', (user_id, category))
        total_spent = cursor.fetchone()[0] or 0
        if total_spent > limit_row[0]:
            return f" Budget exceeded for category '{category}'! Limit: {limit_row[0]}, Spent: {total_spent}"
    return "Within budget"
