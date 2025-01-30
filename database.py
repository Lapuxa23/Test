import sqlite3

class Database:
    def __init__(self, db_path="database.db"):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS homeworks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                homework_number TEXT NOT NULL,
                github_link TEXT NOT NULL
            )
        ''')
        self.conn.commit()

    def save_homework(self, data: dict):

        try:
            self.cursor.execute('''
                INSERT INTO homeworks (name, homework_number, github_link)
                VALUES (?, ?, ?)
            ''', (data["name"], data["homework_number"], data["github_link"]))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Ошибка записи в БД: {e}")
            self.conn.rollback()
            return False

    def get_all_homeworks(self):

        self.cursor.execute("SELECT * FROM homeworks")
        rows = self.cursor.fetchall()
        homeworks = []
        for row in rows:
            homeworks.append({
                "id": row[0],
                "name": row[1],
                "homework_number": row[2],
                "github_link": row[3]
            })
        return homeworks

    def close(self):

        self.conn.close()
