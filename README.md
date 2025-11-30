Smart Task Analyzer

This is a Django + JavaScript based mini-application built for the Software Development Intern Technical Assessment.
The goal is to analyze a list of tasks and recommend what to work on first using a scoring algorithm.

Features

Takes a list of tasks in JSON format.

Calculates a priority score based on urgency, importance, effort, and dependencies.

Returns tasks sorted by score.

Displays results in a simple frontend interface.

Backend built using Django.

API endpoints provided for task analysis.

Scoring Algorithm (tasks/scoring.py)

The scoring logic calculates a score for each task:

Urgency:
If a task is overdue, +100 points.
If due in 3 days or less, +50 points.
If due in 7 days or less, +20 points.

Importance:
importance * 5

Effort:
If effort < 2 hours, +10 points (quick win).

Dependencies:
Each dependency subtracts 10 points.

Project Structure

task-analyzer/
backend/
settings.py
urls.py
tasks/
models.py
scoring.py
views.py
urls.py
frontend/
index.html
styles.css
script.js
manage.py

How To Run The Project

Create and activate a virtual environment:

python -m venv venv
venv\Scripts\activate (Windows)

Install dependencies:

pip install Django
pip install django-cors-headers

Apply migrations:

python manage.py migrate

Start the Django development server:

python manage.py runserver

Open the frontend:
Open frontend/index.html in your browser.
If using VS Code Live Server, the URL will look like:
http://127.0.0.1:5500/frontend/index.html

API Endpoints

POST /api/tasks/analyze/
Accepts a JSON array of tasks.
Returns the same list sorted by score.

GET /api/tasks/suggest/
Returns informational message or future suggestions.

Notes

This project demonstrates:

Clean backend API structure

Vanilla JavaScript frontend integration

Custom algorithm design

Handling of CORS

JSON input validation

Clear full-stack communication