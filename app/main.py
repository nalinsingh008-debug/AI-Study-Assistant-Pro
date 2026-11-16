from datetime import date
from pathlib import Path
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse, FileResponse
from .models import StudySessionCreate
from .repository import StudyRepository
from .analytics import StudyAnalytics
from .predictor import PerformancePredictor
from .automation import ReportAutomation

app = FastAPI(title="AI Study Assistant Pro", version="1.0.0")
repository = StudyRepository()
predictor = PerformancePredictor()
automation = ReportAutomation()

@app.get("/", response_class=HTMLResponse)
def dashboard():
    summary = StudyAnalytics(repository.list_sessions()).summary()
    return f"""
    <!doctype html><html><head><title>AI Study Assistant Pro</title>
    <style>body{{font-family:Arial;margin:40px;background:#f4f7fb;color:#182235}}
    main{{max-width:850px;margin:auto;background:white;padding:28px;border-radius:14px}}
    .stats{{display:flex;gap:16px;flex-wrap:wrap}}.tile{{background:#edf3ff;padding:18px;border-radius:10px;min-width:140px}}
    a{{color:#2457b2}}</style></head><body><main>
    <h1>AI Study Assistant Pro</h1><p>Track study sessions, review analytics and generate reports.</p>
    <div class="stats"><div class="tile"><b>{summary['total_sessions']}</b><br>Sessions</div>
    <div class="tile"><b>{summary['total_hours']}</b><br>Study hours</div>
    <div class="tile"><b>{summary['total_tasks']}</b><br>Tasks completed</div></div>
    <h2>Quick links</h2><p><a href="/docs">Open API documentation</a></p>
    <p><a href="/sessions">View study sessions (JSON)</a></p>
    <p><a href="/analytics">View analytics (JSON)</a></p>
    </main></body></html>
    """

@app.post("/sessions")
def add_session(payload: StudySessionCreate):
    try:
        return repository.add_session(payload)
    except Exception as exc:
        raise HTTPException(status_code=500, detail="Could not save study session") from exc

@app.get("/sessions")
def list_sessions():
    return repository.list_sessions()

@app.get("/analytics")
def analytics():
    return StudyAnalytics(repository.list_sessions()).summary()

@app.post("/predict")
def predict(payload: dict):
    try:
        hours = float(payload["study_hours"])
        tasks = int(payload["tasks_completed"])
        if not 0 <= hours <= 24 or tasks < 0:
            raise ValueError
    except (KeyError, TypeError, ValueError):
        raise HTTPException(status_code=422, detail="Provide study_hours (0-24) and tasks_completed (0 or more)")
    return {"estimated_score": predictor.predict(hours, tasks),
            "note": "Educational estimate only; not a validated exam prediction."}

@app.post("/reports/daily")
def generate_daily_report(report_date: date | None = None):
    path = automation.generate_daily_report(repository.list_sessions(), report_date)
    return {"message": "Report generated", "file": str(path)}

@app.get("/reports/download")
def download_report(report_date: date | None = None):
    report_date = report_date or date.today()
    path = Path("reports") / f"study_report_{report_date.isoformat()}.csv"
    if not path.exists():
        raise HTTPException(status_code=404, detail="Generate the report first")
    return FileResponse(path, media_type="text/csv", filename=path.name)
