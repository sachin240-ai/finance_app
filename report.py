from db import get_db

def generate_report(user_id, year, month=None):
    conn = get_db()
    cursor = conn.cursor()

    if month:
        cursor.execute('''
            SELECT type, SUM(amount) FROM transactions 
            WHERE user_id=? AND strftime('%Y', date)=? AND strftime('%m', date)=? 
            GROUP BY type
        ''', (user_id, str(year), f"{int(month):02}"))
    else:
        cursor.execute('''
            SELECT type, SUM(amount) FROM transactions 
            WHERE user_id=? AND strftime('%Y', date)=? 
            GROUP BY type
        ''', (user_id, str(year)))

    data = cursor.fetchall()
    income = sum(x[1] for x in data if x[0] == 'income')
    expense = sum(x[1] for x in data if x[0] == 'expense')
    savings = income - expense

    return {
        "Income": income,
        "Expenses": expense,
        "Savings": savings
    }
