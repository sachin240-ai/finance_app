from auth import create_user_table, register, login
from finance import create_transactions_table, add_transaction, get_transactions
from report import generate_report
from budget import create_budget_table, set_budget, check_budget
from backup_restore import backup_db, restore_db
from utils import prompt_user_login

def initialize():
    create_user_table()
    create_transactions_table()
    create_budget_table()

def menu(user):
    user_id = user[0]
    while True:
        print("\n1. Add Transaction\n2. View Transactions\n3. Set Budget\n4. Generate Report\n5. Backup\n6. Restore\n7. Logout")
        choice = input("Choice: ")
        if choice == "1":
            t_type = input("Type (income/expense): ")
            category = input("Category: ")
            amount = float(input("Amount: "))
            date = input("Date (YYYY-MM-DD): ")
            add_transaction(user_id, t_type, category, amount, date)
            print(check_budget(user_id, category))
        elif choice == "2":
            for txn in get_transactions(user_id):
                print(txn)
        elif choice == "3":
            category = input("Category: ")
            limit = float(input("Limit: "))
            set_budget(user_id, category, limit)
        elif choice == "4":
            year = input("Year: ")
            month = input("Month (optional): ")
            report = generate_report(user_id, year, month or None)
            print(report)
        elif choice == "5":
            backup_db()
        elif choice == "6":
            restore_db()
        elif choice == "7":
            break

def main():
    initialize()
    while True:
        print("\n--- Personal Finance Manager ---\n1. Register\n2. Login\n3. Exit")
        choice = input("Choice: ")
        if choice == "1":
            uname, pwd = prompt_user_login()
            if register(uname, pwd):
                print("✅ Registration successful.")
            else:
                print("❌ Username already exists.")
        elif choice == "2":
            uname, pwd = prompt_user_login()
            user = login(uname, pwd)
            if user:
                print("✅ Login successful.")
                menu(user)
            else:
                print("❌ Invalid credentials.")
        elif choice == "3":
            break

if __name__ == "__main__":
    main()
