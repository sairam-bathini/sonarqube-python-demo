import sqlite3
import db

# Hardcoded credentials (security issue)
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "password123"  # Avoid hardcoding sensitive data

def login(username, password):
    # Improper authentication (security issue)
    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        print("Login successful!")
    else:
        print("Login failed!")

def search_users(search_term):
    # SQL Injection Vulnerability (security issue)
    query = f"SELECT * FROM users WHERE username LIKE '%{search_term}%'"
    return db.execute_query(query)

if __name__ == "__main__":
    # User input without validation (security issue)
    search_term = input("Search for a username: ")
    print(search_users(search_term))
    
    username = input("Enter username: ")
    password = input("Enter password: ")
    login(username, password)
