from django import forms
from django.contrib.auth.models import User
from .models import Patient, Doctor

class PatientUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['age', 'gender', 'contact']

class DoctorUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['specialization', 'availability']
