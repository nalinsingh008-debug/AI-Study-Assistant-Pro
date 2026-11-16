from datetime import date
from pathlib import Path
from .analytics import StudyAnalytics

class ReportAutomation:
    def __init__(self, output_dir="reports"):
        self.output_dir = Path(output_dir)

    def generate_daily_report(self, sessions, report_date: date | None = None):
        report_date = report_date or date.today()
        daily = [s for s in sessions if str(s["session_date"]) == report_date.isoformat()]
        self.output_dir.mkdir(parents=True, exist_ok=True)
        path = self.output_dir / f"study_report_{report_date.isoformat()}.csv"
        StudyAnalytics(daily).to_csv(path)
        return path
