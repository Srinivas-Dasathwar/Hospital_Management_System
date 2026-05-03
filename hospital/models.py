from django.db import models
from accounts.models import Patient, Doctor

class Appointment(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    )

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='appointments')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='appointments')
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    prescription = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Appointment: {self.patient.user.first_name} with {self.doctor.user.first_name} on {self.date}"
