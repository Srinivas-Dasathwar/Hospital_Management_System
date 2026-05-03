from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import PatientUserForm, PatientForm, DoctorUserForm, DoctorForm
from django.contrib.auth.forms import AuthenticationForm

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

def register_patient(request):
    if request.method == 'POST':
        user_form = PatientUserForm(request.POST)
        patient_form = PatientForm(request.POST)
        if user_form.is_valid() and patient_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user.password)
            user.save()
            patient = patient_form.save(commit=False)
            patient.user = user
            patient.save()
            return redirect('login')
    else:
        user_form = PatientUserForm()
        patient_form = PatientForm()
    return render(request, 'accounts/register.html', {'user_form': user_form, 'patient_form': patient_form, 'role': 'Patient'})

def register_doctor(request):
    if request.method == 'POST':
        user_form = DoctorUserForm(request.POST)
        doctor_form = DoctorForm(request.POST)
        if user_form.is_valid() and doctor_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user.password)
            user.save()
            doctor = doctor_form.save(commit=False)
            doctor.user = user
            doctor.save()
            return redirect('login')
    else:
        user_form = DoctorUserForm()
        doctor_form = DoctorForm()
    return render(request, 'accounts/register.html', {'user_form': user_form, 'patient_form': doctor_form, 'role': 'Doctor'})
