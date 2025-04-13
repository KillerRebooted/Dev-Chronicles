import sqlite3
import os

def track_book(account_loc, book, status):

    # Connect to or create a database file
    conn = sqlite3.connect(os.path.join(account_loc, f"User.db"))
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

def read_data(account_loc, category, page_num):

    # Connect to User.db
    conn = sqlite3.connect(os.path.join(account_loc, "User.db"))
    cursor = conn.cursor()

    # Calculate indices to be extracted based on page number
    limit = 5 # Number of Entries per page
    offset = (page_num-1)*limit

    # Request and Retrieve data from Sqlite3 database
    cursor.execute(f"SELECT * FROM User_Data WHERE status='{category}' LIMIT {limit} OFFSET {offset}")
    retrieved_data = cursor.fetchall()

    return retrieved_data

if __name__ == "__main__":
    read_data(r"D:\Coding Files\Python\Prototype\Bookmark\Data\Accounts\a", "Completed", 2)