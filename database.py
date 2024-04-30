import sqlite3

DB_FILE = "sound_archive.db"

def create_database():
    # Connect to the database (creates a new file if it doesn't exist)
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    # Create the AudioFiles table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS AudioFiles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            path TEXT,
            metadata TEXT
        )
    """)

    # Commit changes and close the connection
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database()
