import sqlite3
from typing import Dict, List, Tuple

class Database:
    def __init__(self, db_path: str = "sqlite_db.db"):
        self.db_path = db_path
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        """Create the posts table if it doesn't exist."""
        try:
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS posts (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    link TEXT NOT NULL,
                    date TEXT NOT NULL,
                    author TEXT NOT NULL
                )
            """)
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error creating table: {e}")

    def insert_data(self, data: Dict[str, str]):
        """Insert a new post into the posts table."""
        try:
            self.cursor.execute("""
                INSERT INTO posts (title, link, date, author)
                VALUES (:title, :link, :date, :author)
            """, data)
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error inserting data: {e}")

    def get_data(self, keyword: str) -> List[Tuple]:
        """Retrieve posts that match the given keyword."""
        try:
            self.cursor.execute("""
                SELECT * FROM posts
                WHERE title LIKE ?
            """, ('%' + keyword + '%',))
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error fetching data: {e}")
            return []

    def close(self):
        """Close the database connection."""
        try:
            self.conn.close()
        except sqlite3.Error as e:
            print(f"Error closing the database: {e}")

