from django.db import models
from django.contrib.auth.models import User

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=(('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')))
    contact = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=100)
    availability = models.CharField(max_length=200, help_text="e.g., Mon-Fri 9AM-5PM")

    def __str__(self):
        return f"Dr. {self.user.first_name} {self.user.last_name} ({self.specialization})"
