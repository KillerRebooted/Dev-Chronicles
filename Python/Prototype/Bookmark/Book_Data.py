import sqlite3

# Connect to or create a database file
conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY,
    title TEXT,
    author TEXT
)
""")

# Insert data
cursor.execute("INSERT INTO books (title, author) VALUES (?, ?)", ("1984", "George Orwell"))

# Fetch data
cursor.execute("SELECT * FROM books")
print(cursor.fetchall())

conn.commit()
conn.close()