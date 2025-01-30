import sqlite3


class Database:
    def __init__(self, path: str):
        self.path = path

    def create_tables(self):
        with sqlite3.connect(self.path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS homework(
                name TEXT,
                number INTEGER,
                link TEXT
            )
            """)
            conn.commit()

    def send_homework(self, data: dict):
        with sqlite3.connect(self.path) as conn:
            conn.execute(
                """
                    INSERT INTO homework(name, number, link)
                    VALUES (?, ?, ?)
                """,
                (data["name"], data["number"], data["link"]))
            conn.commit()
