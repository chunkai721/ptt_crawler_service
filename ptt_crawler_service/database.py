## database.py
import sqlite3
from typing import Dict

class Database:
    def __init__(self, db_path: str = "sqlite_db_path.db"):
        self.db_path = db_path
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
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

    def insert_data(self, data: Dict[str, str]):
        self.cursor.execute("""
            INSERT INTO posts (title, link, date, author)
            VALUES (:title, :link, :date, :author)
        """, data)
        self.conn.commit()

    def get_data(self, keyword: str):
        self.cursor.execute("""
            SELECT * FROM posts
            WHERE title LIKE ?
        """, ('%' + keyword + '%',))
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()
