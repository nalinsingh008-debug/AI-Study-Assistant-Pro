import pandas as pd

class StudyAnalytics:
    def __init__(self, sessions):
        self.frame = pd.DataFrame(sessions)

    def summary(self):
        if self.frame.empty:
            return {
                "total_sessions": 0, "total_hours": 0.0,
                "total_tasks": 0, "subject_hours": {}
            }
        grouped = self.frame.groupby("subject")["study_hours"].sum()
        return {
            "total_sessions": int(len(self.frame)),
            "total_hours": round(float(self.frame["study_hours"].sum()), 2),
            "total_tasks": int(self.frame["tasks_completed"].sum()),
            "subject_hours": {str(k): round(float(v), 2) for k, v in grouped.items()}
        }

    def to_csv(self, path):
        self.frame.to_csv(path, index=False)
        return str(path)
