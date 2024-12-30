# users/models.py
from django.db import models
from django.contrib.auth.models import User

class HealthRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="health_records")
    title = models.CharField(max_length=100)  # e.g., "Blood Test"
    description = models.TextField()          # e.g., "Test for CBC and cholesterol"
    date = models.DateField()                 # e.g., Date of the record
    data = models.JSONField()                 # e.g., Lab results or other details

    def __str__(self):
        return f"{self.title} - {self.user.username}"
