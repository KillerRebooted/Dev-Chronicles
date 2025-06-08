import sqlite3
import os

limit = 5 # Number of Entries per page

def create_table(cursor):
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
        page_count TEXT,
        description TEXT,
        maturity_rating TEXT
    )
    """)

def track_book(account_loc, book, status):

    # Connect to or create a database file
    conn = sqlite3.connect(os.path.join(account_loc, f"User.db"))
    cursor = conn.cursor()

    # Create Table
    create_table(cursor)

    # Check Existence of Book in Table
    cursor.execute(f'''SELECT 1 FROM User_Data WHERE id = "{book['id']}"''')
    exists = cursor.fetchone() is not None

    if (not exists) and (status != "Remove From List"):
        # Insert Data
        cursor.execute("INSERT INTO User_Data VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (book['id'], status, book["thumbnail"], book['title'], book['authors'], book['language'], book['isbn10'], book['isbn13'], book['publisher'], book['publish_date'], book['categories'], book['page_count'], book['description'], book['maturity_rating']))
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

    # Create Table
    create_table(cursor)

    # Get Table Description
    cursor.execute("PRAGMA table_info(User_Data)")

    # Get column names
    columns = [description[1] for description in cursor.fetchall()]

    # Calculate indices to be extracted based on page number
    offset = (page_num-1)*limit

    # Request and Retrieve data from Sqlite3 database
    cursor.execute(f"SELECT * FROM User_Data WHERE status='{category}' LIMIT {limit} OFFSET {offset}")
    retrieved_data = cursor.fetchall()       

    return_dict = {}

    if retrieved_data != []:
        for c in range(len(retrieved_data[0])):
            for r in range(len(retrieved_data)):
                return_dict[columns[c]] = return_dict.get(columns[c], [])+[retrieved_data[r][c]]

    return return_dict

def get_total_pages(account_loc, category):
    
    # Connect to User.db
    conn = sqlite3.connect(os.path.join(account_loc, "User.db"))
    cursor = conn.cursor()

    # Create Table
    create_table(cursor)

    # Get total items in category
    cursor.execute(f"SELECT COUNT(*) FROM User_Data WHERE status='{category}'")
    total_items = cursor.fetchall()[0][0]

    if total_items%limit == 0:
        return total_items//limit
    else:
        return total_items//limit + 1

if __name__ == "__main__":
    print(read_data(r"D:\Coding Files\Python\Prototype\Bookmark\Data\Accounts\a", "Plan to Read", 1))