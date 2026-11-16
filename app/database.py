import os
import sqlite3
from pathlib import Path

DEFAULT_DB = Path(os.getenv("STUDY_DB_PATH", "study_assistant.db"))

def get_connection(db_path: str | Path | None = None) -> sqlite3.Connection:
    path = Path(db_path) if db_path else DEFAULT_DB
    path.parent.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(path)
    connection.row_factory = sqlite3.Row
    return connection

def initialize_database(db_path: str | Path | None = None) -> None:
    with get_connection(db_path) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS study_sessions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                subject TEXT NOT NULL,
                study_hours REAL NOT NULL CHECK(study_hours >= 0),
                tasks_completed INTEGER NOT NULL CHECK(tasks_completed >= 0),
                session_date TEXT NOT NULL
            )
        """)
