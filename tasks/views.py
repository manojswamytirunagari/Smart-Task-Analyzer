import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .scoring import calculate_task_score

@csrf_exempt
def analyze_tasks(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST only"}, status=400)

    try:
        data = json.loads(request.body.decode("utf-8"))
    except Exception:
        return JsonResponse({"error": "Invalid JSON"}, status=400)

    if not isinstance(data, list):
        return JsonResponse({"error": "Expected a list of tasks"}, status=400)

    scored_tasks = []
    for t in data:
        score = calculate_task_score(t)
        t["score"] = score
        scored_tasks.append(t)

    # Sort high score → low score
    sorted_tasks = sorted(scored_tasks, key=lambda x: x["score"], reverse=True)

    return JsonResponse(sorted_tasks, safe=False)


@csrf_exempt
def suggest_tasks(request):
    """
    Returns the top 3 recommended tasks with explanations.
    """
    if request.method != "GET":
        return JsonResponse({"error": "GET only"}, status=400)

    # Example: This endpoint ideally pulls real tasks from DB.
    # For now, return info message.
    return JsonResponse({"message": "Suggestions require task input. Use /analyze/."})
