# AI Study Assistant Pro

A Python study-tracking application combining FastAPI, SQLite, Pandas analytics,
a scikit-learn prediction demonstration, and automated CSV reports.

## Features
- Add and view study sessions.
- Store study data in SQLite.
- Analyse total hours, tasks, sessions, and subject-wise hours with Pandas.
- Estimate a study score using a small illustrative Linear Regression model.
- Generate daily CSV reports.
- Browser dashboard and interactive REST API documentation.
- Input validation, error handling, OOP structure, and Pytest tests.

> The predictor is an educational demonstration trained on a small illustrative
> dataset. It is not an exam result or a scientifically validated prediction.

## Requirements
- Python 3.10 or newer

## Install (Windows PowerShell / VS Code terminal)
```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```
If activation is blocked, use Command Prompt:
```cmd
.venv\Scripts\activate.bat
```

## Run
```powershell
python -m uvicorn app.main:app --reload
```
Open http://127.0.0.1:8000 for the dashboard and http://127.0.0.1:8000/docs
for API documentation.

## Test
```powershell
python -m pytest -v
```

## API endpoints
| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/` | Dashboard |
| POST | `/sessions` | Save a study session |
| GET | `/sessions` | List sessions |
| GET | `/analytics` | Pandas analytics summary |
| POST | `/predict` | Estimate a study score |
| POST | `/reports/daily` | Generate a dated CSV report |
| GET | `/reports/download` | Download the generated CSV report |

Example `POST /sessions` JSON:
```json
{
  "subject": "Python",
  "study_hours": 2.5,
  "tasks_completed": 4,
  "session_date": "2026-11-16"
}
```

## Project structure
```text
ai_study_assistant_pro/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── repository.py
│   ├── analytics.py
│   ├── predictor.py
│   └── automation.py
├── tests/
│   └── test_app.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Screenshot
After starting the app, open `http://127.0.0.1:8000` and take a screenshot
of the dashboard. Save it as `screenshots/dashboard.png` and add it to the
repository before resubmitting, so the screenshot shows the running application.

## Architecture
- `StudySessionCreate` validates incoming data.
- `StudyRepository` handles SQLite database operations.
- `StudyAnalytics` uses Pandas for summaries and CSV export.
- `PerformancePredictor` encapsulates the Scikit-learn model.
- `ReportAutomation` creates dated CSV reports.
- FastAPI exposes the dashboard and API endpoints.

## Submission checklist
1. Upload the contents of this folder to the same GitHub repository.
2. Confirm that `app/` and `tests/` folders appear in GitHub.
3. Confirm `requirements.txt` and this README are present.
4. Run the application and tests locally.
5. Add a screenshot of the running dashboard.
6. Resubmit the same GitHub repository link on Yunova.
