from datetime import date, datetime

def parse_date(value):
    """Accepts both string (YYYY-MM-DD) and date object."""
    if isinstance(value, date):
        return value
    try:
        return datetime.strptime(value, "%Y-%m-%d").date()
    except Exception:
        return None


def calculate_task_score(task):
    """
    Calculates a numerical priority score for a task.
    Higher score = higher priority.
    """

    score = 0
    today = date.today()

    # ---- 1. Urgency Score ----
    due = parse_date(task.get("due_date"))
    if due:
        days_until_due = (due - today).days
        if days_until_due < 0:
            score += 100     # Overdue
        elif days_until_due <= 3:
            score += 50      # Very close
        elif days_until_due <= 7:
            score += 20      # Within a week

    # ---- 2. Importance Score ----
    importance = task.get("importance", 5)
    score += importance * 5

    # ---- 3. Effort Score ---- (quick wins)
    effort = task.get("estimated_hours", 1)
    if effort < 2:
        score += 10

    # ---- 4. Dependency Penalty ----
    dependencies = task.get("dependencies", [])
    if dependencies:
        score -= len(dependencies) * 10

    return score
