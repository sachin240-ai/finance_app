import shutil

def backup_db():
    shutil.copyfile('finance.db', 'finance_backup.db')
    print("🔄 Backup completed.")

def restore_db():
    shutil.copyfile('finance_backup.db', 'finance.db')
    print("✅ Restore completed.")
