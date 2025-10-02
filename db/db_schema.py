def create_tables(db):
    db.execute("""
            CREATE TABLE IF NOT EXISTS files (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                filename TEXT NOT NULL,
                filepath TEXT NOT NULL,
                uploaded_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """)
