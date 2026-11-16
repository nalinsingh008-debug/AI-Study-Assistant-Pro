from datetime import date
from .database import get_connection, initialize_database

class StudyRepository:
    def __init__(self, db_path=None):
        self.db_path = db_path
        initialize_database(self.db_path)

    def add_session(self, session):
        with get_connection(self.db_path) as conn:
            cursor = conn.execute(
                """INSERT INTO study_sessions
                   (subject, study_hours, tasks_completed, session_date)
                   VALUES (?, ?, ?, ?)""",
                (session.subject, session.study_hours, session.tasks_completed,
                 session.session_date.isoformat())
            )
            row = conn.execute(
                "SELECT * FROM study_sessions WHERE id = ?", (cursor.lastrowid,)
            ).fetchone()
            return dict(row)

    def list_sessions(self):
        with get_connection(self.db_path) as conn:
            rows = conn.execute(
                "SELECT * FROM study_sessions ORDER BY session_date DESC, id DESC"
            ).fetchall()
            return [dict(row) for row in rows]

    def sessions_for_date(self, session_date: date):
        with get_connection(self.db_path) as conn:
            rows = conn.execute(
                "SELECT * FROM study_sessions WHERE session_date = ? ORDER BY id",
                (session_date.isoformat(),)
            ).fetchall()
            return [dict(row) for row in rows]
