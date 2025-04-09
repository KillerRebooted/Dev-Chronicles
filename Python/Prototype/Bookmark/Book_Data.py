import sqlite3
import os

def track_book(account_loc, book, status):

    # Get Username from Account Folder Path
    user = os.path.basename(account_loc)

    # Connect to or create a database file
    conn = sqlite3.connect(os.path.join(account_loc, f"{user}.db"))
    cursor = conn.cursor()

    # Create Table

    cursor.execute(f"""
    CREATE TABLE IF NOT EXISTS User_Data (
        id CHAR(12) PRIMARY KEY,
        status TEXT,
        thumbnail TEXT,
        title TEXT,
        authors TEXT,
        language TEXT,
        isbn10 CHAR(10),
        isbn13 CHAR(13),
        publisher TEXT,
        publish_date TEXT,
        categories TEXT,
        description TEXT,
        maturity_rating TEXT
    )
    """)

    # Check Existence of Book in Table
    cursor.execute(f'''SELECT 1 FROM User_Data WHERE id = "{book['id']}"''')
    exists = cursor.fetchone() is not None

    if (not exists) and (status != "Remove From List"):
        # Insert Data
        cursor.execute(f"""INSERT INTO User_Data VALUES ("{book['id']}", "{status}", "{book["thumbnail"]}", "{book['title']}", "{book['authors']}", "{book['language']}", "{book['isbn10']}", "{book['isbn13']}", "{book['publisher']}", "{book['publish_date']}", "{book['categories']}", "{book['description']}", "{book['maturity_rating']}")""")
    elif (exists) and (status == "Remove From List"):
        # Delete Tuple in case Remove requested
        cursor.execute(f"DELETE FROM User_Data WHERE id = '{book["id"]}'")
    elif (exists) and (status != "Remove From List"):
        # Update Status
        cursor.execute(f'''UPDATE User_Data SET status = '{status}' WHERE id = "{book['id']}"''')

    conn.commit()
    conn.close()