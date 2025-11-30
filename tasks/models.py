from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    due_date = models.DateField()
    estimated_hours = models.IntegerField(default=1)
    importance = models.IntegerField(default=5)  # scale 1–10

    # Dependencies stored as list of task IDs
    dependencies = models.JSONField(default=list, blank=True)

    def __str__(self):
        return self.title
