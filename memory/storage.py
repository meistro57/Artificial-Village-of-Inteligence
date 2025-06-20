import sqlite3
from pathlib import Path
from typing import Any, Optional

DB_FILE = Path(__file__).resolve().parent / "memory.db"

class Memory:
    def __init__(self, db_path: Path = DB_FILE):
        self.conn = sqlite3.connect(db_path)
        self._ensure_table()

    def _ensure_table(self) -> None:
        cur = self.conn.cursor()
        cur.execute(
            "CREATE TABLE IF NOT EXISTS memory (key TEXT PRIMARY KEY, value TEXT)"
        )
        self.conn.commit()

    def store(self, key: str, value: Any) -> None:
        cur = self.conn.cursor()
        cur.execute(
            "REPLACE INTO memory (key, value) VALUES (?, ?)", (key, str(value))
        )
        self.conn.commit()

    def get(self, key: str) -> Optional[str]:
        cur = self.conn.cursor()
        cur.execute("SELECT value FROM memory WHERE key = ?", (key,))
        row = cur.fetchone()
        return row[0] if row else None

    def close(self) -> None:
        self.conn.close()
