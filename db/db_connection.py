import sqlite3

class Database:
    def __init__(self, db_path="database.db"):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor() 

    def execute(self, query, params=()):
        cursor = self.conn.execute(query, params)
        self.conn.commit()
        return cursor
    
    def fetchone(self, query, params=()):
        self.cursor.execute(query, params)
        return self.cursor.fetchone()
    
    def fetchall(self, query, params=()):
        return self.conn.execute(query, params).fetchall()

    def close(self):
        self.conn.close()
