from database import get_connection
import sqlite3

class NoteRepository:

    def find_all(self):
        conn = get_connection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM notes")
        rows = cursor.fetchall()
        conn.close()
        return rows

    def find_by_id(self, note_id):
        conn = get_connection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM notes WHERE id = ?", (note_id,))
        row = cursor.fetchone()
        conn.close()
        return row

    def save(self, title, content):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO notes (title, content) VALUES (?, ?)",
            (title, content)
        )
        conn.commit()
        conn.close()

    def delete(self, note_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM notes WHERE id = ?", (note_id,))
        conn.commit()
        conn.close()
    
    def update(self, note_id, title, content):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE notes SET title = ?, content = ? WHERE id = ?",
            (title, content, note_id)
    )
        conn.commit()
        conn.close()

