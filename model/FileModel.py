import os
import shutil
from db.db_connection import Database

class FileModel:
    def __init__(self, db: Database, upload_dir="upload"):
        self.db = db
        self.upload_dir = upload_dir
        os.makedirs(upload_dir, exist_ok=True)

    def save_file(self, source_path):
        filename = os.path.basename(source_path)
        target_path = os.path.join(self.upload_dir, filename)
        shutil.copy(source_path, target_path)

        self.db.execute(
            "INSERT INTO files (filename, filepath) VALUES (?, ?)",
            (filename, target_path)
        )
        return filename, target_path

    def get_all_files(self):
        return self.db.fetchall(
            "SELECT id, filename, filepath FROM files ORDER BY uploaded_at DESC"
        )

    def delete_file(self, file_id):
        result = self.db.fetchone(
            "SELECT filepath FROM files WHERE id = ?", (file_id,)
        )
        if result:
            filepath = result[0]
            if os.path.exists(filepath):
                os.remove(filepath)
        self.db.execute("DELETE FROM files WHERE id = ?", (file_id,))
