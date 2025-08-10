import sqlite3
import hashlib
from db import get_db

def create_user_table():
    Connect = get_db()
    cursor = Connect.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    Connect.commit()

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register(username, password):
    Connect = get_db()
    cursor = Connect.cursor()
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hash_password(password)))
        Connect.commit()
        return True
    except sqlite3.IntegrityError:
        return False

def login(username, password):
    Connect = get_db()
    cursor = Connect.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, hash_password(password)))
    return cursor.fetchone()
